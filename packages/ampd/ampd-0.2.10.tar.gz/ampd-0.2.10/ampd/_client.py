# coding: utf-8

# Asynchronous Music Player Daemon client library for Python

# Copyright (C) 2015 Itaï BEN YAACOV

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import logging
import asyncio
import urllib.parse
import sys
import decorator
import contextlib
import traceback

from . import _request
from . import errors


_logger = logging.getLogger(__name__.split('.')[0])


class _Task(asyncio.Task):
    def __init__(self, future, *, loop=None):
        self._caller_filename, self._caller_line, self._caller_function, self._caller_text = traceback.extract_stack()[-4]
        self._future = future
        super().__init__(self.wrap(), loop=loop)

    async def wrap(self):
        try:
            await self._future
        except asyncio.CancelledError as e:
            pass
        except Exception:
            print('While awaiting {}:'.format(self._future))
            sys.excepthook(*sys.exc_info())

    def _repr_info(self):
        info = super()._repr_info()
        return info[:1] + [repr(self._future)] + info[2:]


@decorator.decorator
def task(func, *args, **kwargs):
    """
    Decorator for AMPD task functions.

    Wraps in a Task which will accept cancellation as normal termination.
    """
    return _Task(func(*args, **kwargs))


class AMPDProtocol(asyncio.Protocol):
    def __init__(self, process_reply, disconnect_cb):
        super().__init__()
        self._process_reply = process_reply
        self._disconnect_cb = disconnect_cb

    def connection_made(self, transport):
        print("Protocol connection made")
        self._transport = transport
        self._lines = []
        self._incomplete_line = b''

    def connection_lost(self, exc):
        print("Protocol connection lost")
        if self._disconnect_cb is not None:
            asyncio.ensure_future(self._disconnect_cb(Client.DISCONNECT_ERROR))

    def data_received(self, data):
        new_lines = (self._incomplete_line + data).split(b'\n')
        for line in new_lines[:-1]:
            self._lines.append(line)
            if line.startswith(b'OK') or line.startswith(b'ACK'):
                asyncio.ensure_future(self._process_reply(self._lines))
                self._lines = []
        self._incomplete_line = new_lines[-1]


class Executor(object):
    """
    Generates AMPD requests.
    """

    def __init__(self, client_or_parent):
        if isinstance(client_or_parent, Executor):
            self._parent = client_or_parent
            self._client = client_or_parent._client
            self._parent._children.append(self)
        else:
            self._parent = None
            self._client = client_or_parent
        self._children = []
        self._requests = []
        self._connect_cb_func = self._disconnect_cb_func = None

    async def close(self):
        _logger.debug("Closing executor {}".format(self))
        if not self._client:
            return
        while self._children:
            await self._children[0].close()
        if self._requests:
            for request in self._requests:
                request.cancel()
            await asyncio.wait(self._requests)
        if self._parent:
            self._parent._children.remove(self)
            self._parent = None
        self._client = None
        self._connect_cb_func = self._disconnect_cb_func = None
        _logger.debug("Executor closed")

    def sub_executor(self):
        "Return a child Executor."
        return Executor(self)

    def set_callbacks(self, connect_cb, disconnect_cb):
        self._connect_cb_func = connect_cb
        self._disconnect_cb_func = disconnect_cb
        if self.get_is_connected() and connect_cb is not None:
            connect_cb()

    def _connect_cb(self):
        if self._connect_cb_func is not None:
            self._connect_cb_func()
        for child in self._children:
            child._connect_cb()

    def _disconnect_cb(self, reason, message):
        for child in self._children:
            child._disconnect_cb(reason, message)
        if self._disconnect_cb_func is not None:
            self._disconnect_cb_func(reason, message)

    def get_is_connected(self):
        return self._client._state == Client.STATE_CONNECTED

    def get_protocol_version(self):
        return self._client.protocol_version

    def __getattr__(self, name):
        return _request.Request._new_request(self, name)

    def _log_request(self, request):
        if self._client is None:
            raise errors.ConnectionError
        _logger.debug("Appending request {} of task {} to {}".format(request, asyncio.Task.current_task(), self))
        self._requests.append(request)
        request.add_done_callback(self._unlog_request)
        if isinstance(request, _request.RequestPassive):
            self._client._wait(request)
        else:
            self._client._send(request)

    def _unlog_request(self, request):
        self._requests.remove(request)


class Client(object):
    """
    Establishes connection with the MPD server.
    """

    STATE_DISCONNECTED = 0
    STATE_CONNECTING = 1
    STATE_CONNECTED = 2

    DISCONNECT_NOT_CONNECTED = 0
    DISCONNECT_FAILED_CONNECT = 1
    DISCONNECT_ERROR = 2
    DISCONNECT_REQUESTED = 3
    DISCONNECT_RECONNECT = 4
    DISCONNECT_SHUTDOWN = 5
    DISCONNECT_PASSWORD = 6

    def __init__(self, *, excepthook=None):
        """
        Initialize a client.

        excepthook - override sys.excepthook for exceptions raised in workers.
        """
        self.executor = Executor(self)
        self._excepthook = excepthook
        self._waiting_list = []
        self._host = self._port = self._password = None

        self._state = self.STATE_DISCONNECTED
        self.protocol_version = None

        self._run_lock = asyncio.Lock()

    def __del__(self):
        _logger.debug("Deleting {}".format(self))

    async def close(self):
        """
        Close all workers and worker groups, disconnect from server.
        """
        _logger.debug("Closing client")
        await self.executor.close()
        await self.disconnect_from_server(self.DISCONNECT_SHUTDOWN)
        _logger.debug("Client closed")

    async def connect_to_server(self, host=None, port=6600, password=None):
        """
        host     - '[password@]hostname[:port]'.  Default to $MPD_HOST or 'localhost'.
        port     - Ignored if given in the 'host' argument.
        password - Ignored if given in the 'host' argument.
        """

        netloc = urllib.parse.urlsplit('//' + (host or os.environ.get('MPD_HOST', 'localhost')))

        self._host = netloc.hostname
        self._port = netloc.port or port
        self._password = netloc.username or password

        await self.reconnect_to_server()

    async def reconnect_to_server(self):
        """
        Connect to server with previous host / port / password.
        """
        await self.disconnect_from_server(self.DISCONNECT_RECONNECT)
        self._state = self.STATE_CONNECTING
        self._connecting = _Task(self._connect())

    async def _connect(self):
        assert self._state == self.STATE_CONNECTING

        try:
            _logger.debug("Connecting to {}:{}".format(self._host, self._port))
            self._transport, self._protocol = await asyncio.get_event_loop().create_connection(self._protocol_factory, self._host, self._port)
            _logger.debug("Connected")
            print("Connected")
        except OSError as exc:
            self._state = self.STATE_DISCONNECTED
            self.executor._disconnect_cb(self.DISCONNECT_FAILED_CONNECT, str(exc))
            return

        self._state = self.STATE_CONNECTED

        self._is_idle = False
        welcome = _request.RequestWelcome(self.executor)
        self._active_queue = [welcome]
        self._connect_task(welcome)

    async def disconnect_from_server(self, _reason=DISCONNECT_REQUESTED, _message=None):
        if self._state == self.STATE_DISCONNECTED:
            return

        if self._state == self.STATE_CONNECTING:
            self._connecting.cancel()
        else:
            self._protocol._disconnect_cb = None
            self._transport.close()
            self.protocol_version = None
            for request in self._active_queue + self._waiting_list:
                if not request.done():
                    request.cancel()
            del self._active_queue, self._transport, self._protocol
            print("Disconnected, deleted")

        self._state = self.STATE_DISCONNECTED
        self.executor._disconnect_cb(_reason, _message)

    async def _process_reply(self, reply):
        if '_active_queue' not in vars(self):
            print("WTF?")
        if not self._active_queue:
            await self.disconnect_from_server(self.DISCONNECT_ERROR)
            return

        request = self._active_queue.pop(0)
        request._process_reply(reply)
        if not self._active_queue:
            self._active = False
            self._idle_task()

    def _protocol_factory(self):
        return AMPDProtocol(self._process_reply, self.disconnect_from_server)

    def _send(self, request):
        self._active = True
        if self._state != self.STATE_CONNECTED:
            raise errors.ConnectionError
        if isinstance(request, _request.RequestIdle):
            self._is_idle = True
        elif self._is_idle:
            self._transport.write(b'noidle\n')
            _logger.debug("Unidle")
            self._is_idle = False
        self._transport.write(request._commandline.encode('utf-8') + b'\n')
        _logger.debug("Write : " + request._commandline)
        self._active_queue.append(request)

    def _wait(self, request):
        # self._active = True
        event = self._current_events() & request._event_mask
        if event:
            request.set_result(event)
        else:
            self._waiting_list.append(request)
            request.add_done_callback(self._waiting_list.remove)

    def _current_events(self):
        return (_request.Event.IDLE if self._state == self.STATE_CONNECTED and self._is_idle else 0) | (_request.Event.CONNECT if self._state == self.STATE_CONNECTED else 0)

    @task
    async def _connect_task(self, welcome):
        self.protocol_version = await welcome
        if self._password:
            try:
                await self.executor.password(self._password)
            except errors.ReplyError:
                self.disconnect_from_server(self.DISCONNECT_PASSWORD)
                return
        self.executor._connect_cb()
        self._event(_request.Event.CONNECT)

    def _unidle(self, request):
        self._is_idle = False

    @task
    async def _idle_task(self):
        if self._active or self._event(_request.Event.IDLE, True):
            return
        _logger.debug("Going idle")
        request = _request.RequestIdle(self.executor)
        request.add_done_callback(self._unidle)
        event = sum(_request.Event[subsystem.upper()] for subsystem in await request)
        if event:
            self._event(event)

    def _event(self, event, one=False):
        for request in list(self._waiting_list):
            reply = request._event_mask & event
            if reply:
                self._active = True
                request.set_result(reply)
                if one:
                    return True
        return False


class ServerProperties(object):
    """
    Keeps track of various properties of the server:
    - status
    - current_song
    - state
    - volume
    - time
    - elapsed
    - bitrate
    - option-X, for X in consume, random, repeat, single

    Assignment to volume is reflected in the server.

    Do not use this -- use ServerPropertiesGLib instead.
    """

    OPTION_NAMES = ['consume', 'random', 'repeat', 'single']

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value
        if not self._blocking:
            self._set_server_volume()

    @task
    async def _set_server_volume(self):
        if self._setting_volume:
            self._setting_volume.cancel()
        task = self._setting_volume = asyncio.Task.current_task()
        value = self.volume
        _logger.debug("Setting volume to {} at {}".format(value, task))
        try:
            while True:
                try:
                    await self.ampd.setvol(value)
                except errors.ReplyError:
                    await self.ampd.idle(_request.Event.PLAYER)
                    continue
                status = await self.ampd.status()
                if int(status['volume']) == value:
                    break
                await self.ampd.idle(_request.Event.PLAYER | _request.Event.MIXER)
                _logger.debug("Sucessfully set volume to {} at {}".format(value, task))
        finally:
            if self._setting_volume == task:
                self._setting_volume = None

    def __init__(self, client):
        self.ampd = client.executor.sub_executor()
        self.ampd.set_callbacks(self._connect_cb, self._disconnect_cb)
        self._setting_volume = None
        self._reset()

    @contextlib.contextmanager
    def _block(self):
        self._blocking = True
        try:
            yield
        finally:
            self._blocking = False

    def _reset(self):
        with self._block():
            self._error = None
            self.current_song = {}
            self.status = {}
            self.state = ''
            self.volume = -1
            self.time = 0
            self.elapsed = 0
            self.bitrate = None
            self.updating_db = None

    @task
    async def _connect_cb(self):
        while True:
            with self._block():
                self.status = await self.ampd.status()
                self._status_updated()
                if self.state == 'stop':
                    if self.current_song:
                        self.current_song = {}
                else:
                    new_current_song = await self.ampd.currentsong()
                    if self.current_song != new_current_song:
                        self.current_song = new_current_song
            await self.ampd.idle(_request.Event.PLAYER | _request.Event.MIXER | _request.Event.OPTIONS | _request.Event.UPDATE, timeout=(int(self.elapsed + 1.5) - self.elapsed) if self.state == 'play' else 30)

    def _status_properties(self):
        properties = {name: self.status.get(name) for name in ('state', 'bitrate', 'updating_db')}
        volume = int(self.status['volume'])
        if not self._setting_volume and volume != -1:
            properties['volume'] = volume
        if 'time' in self.status:
            times = self.status['time'].split(':')
            properties['time'] = int(times[1])
            properties['elapsed'] = float(self.status['elapsed'])
        else:
            properties['time'] = 0
            properties['elapsed'] = 0.0
        for name in self.OPTION_NAMES:
            properties['option_' + name] = bool(int(self.status[name]))
        return properties

    def _status_updated(self):
        for key, value in self._status_properties().items():
            if getattr(self, key) != value:
                setattr(self, key, value)

    def _disconnect_cb(self, reason, message):
        _logger.debug("Server properties disconnected.")
        self._reset()
