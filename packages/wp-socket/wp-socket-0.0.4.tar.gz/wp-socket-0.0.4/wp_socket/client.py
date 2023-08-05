import asyncio

import logging

_CONNECTION_TIMEOUT = 5.0
_READ_TIMEOUT = 5.0
_QUEUE_WAIT_TIMEOUT = 1.0
_DEFAULT_READ_BUFFER = 512  # 512 bytes

_LOGGER = logging.getLogger(__name__)

class WpSocketClient:
    _reader: asyncio.StreamReader
    _writer: asyncio.StreamWriter

    def __init__(self, host: str, port: int, async_packets_handler):
        self._host = host
        self._port = port
        self._reader: asyncio.StreamReader
        self._wait_tasks = None
        self._async_receive_handler = async_packets_handler

        self._loop = asyncio.get_event_loop()
        self._receive_packet_queue = asyncio.Queue()
        self._send_packet_queue = asyncio.Queue()

        self._connected = None
        self._retry_cnt = 0

    async def async_on_connected(self):
        _LOGGER.debug(f'connected {self._host}')

    async def async_connect(self) -> bool:
        await self.async_wait_for_disconnect()

        _LOGGER.debug(f'connecting to server {self._host}')
        try:
            asyncio.set_event_loop(self._loop)
            conn_task = asyncio.open_connection(self._host, self._port)
            self._reader, self._writer = await asyncio.wait_for(conn_task, timeout=_CONNECTION_TIMEOUT)
            self._connected = True
            self._retry_cnt = 0

            self._loop.create_task(self.async_on_connected())

            tasks = [self._loop.create_task(self._async_reader_handler()),
                     self._loop.create_task(self._async_reader()),
                     self._loop.create_task(self._async_writer())]
            self._wait_tasks = asyncio.wait(tasks)
            return True
        except Exception as ex:
            _LOGGER.error(f'connection error, {self._host}, {str(ex)}')
            self.disconnect()
        return False

    async def _async_reconnect(self):
        wait_time = self._retry_cnt * 5 if self._retry_cnt < 12 else 60
        _LOGGER.debug(f'reconnect connect, wait {wait_time}s')
        await asyncio.sleep(wait_time)
        self._retry_cnt += 1
        if not await self.async_connect():
            await self._async_reconnect()

    async def async_send_packet(self, packet: bytes):
        await self._send_packet_queue.put(packet)

    async def _async_reader_handler(self):
        _LOGGER.debug('message handler start')
        while self._connected:
            try:
                packets = await asyncio.wait_for(self._receive_packet_queue.get(), timeout=_QUEUE_WAIT_TIMEOUT)
                await self._async_receive_handler(packets)
            except asyncio.TimeoutError:
                continue
            except Exception as ex:
                _LOGGER.error(f'message handler error, {ex}')

        _LOGGER.debug('message handler end ')

    async def _async_reader(self):
        _LOGGER.debug('reader start')
        while self._connected:
            try:
                data = await asyncio.wait_for(self._reader.read(_DEFAULT_READ_BUFFER), timeout=_READ_TIMEOUT)
                if not data:
                    self._loop.create_task(self._async_reconnect())
                    break

                _LOGGER.debug(f'Received [{len(data)}]: {data.hex()}')
                await self._receive_packet_queue.put(data)
            except Exception as ex:
                _LOGGER.error(f'reader error, {ex}')
                self._loop.create_task(self._async_reconnect())
                break
        _LOGGER.debug('reader end')

    async def _async_writer(self):
        _LOGGER.debug('writer start')
        while self._connected:
            try:
                packet = await asyncio.wait_for(self._send_packet_queue.get(), timeout=_QUEUE_WAIT_TIMEOUT)
                self._writer.write(packet)
                await self._writer.drain()
                _LOGGER.debug(f'Send [{len(packet)}]: {packet.hex()}')
            except asyncio.TimeoutError:
                continue
            except Exception as ex:
                _LOGGER.error(f'writer error, {ex}')
                self._loop.create_task(self._async_reconnect())
                break
        _LOGGER.debug('writer end')

    async def async_wait_for_disconnect(self):
        self.disconnect()
        if self._wait_tasks is None:
            return
        await self._wait_tasks
        self._wait_tasks = None

    def disconnect(self):
        if not self._connected:
            return
        self._connected = False
        if not self._loop.is_closed():
            self._writer.close()

    def __del__(self):
        self.disconnect()
