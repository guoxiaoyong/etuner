# Copyright (c) 2019 Xiaoyong Guo

import logging
import pyaudio
from concurrent.futures import ThreadPoolExecutor

import numpy as np


class AudioRecorder(object):
    def __init__(
        self,
        *,
        rate=22050,
        frames_per_buffer=2048,
        use_async=False,
    ):
        self._pa = pyaudio.PyAudio()
        self._stream = self._pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=rate,
            input=True,
            frames_per_buffer=frames_per_buffer)
        self._logger = logging.getLogger('AudioRecorder')
        self._executor = None
        if use_async:
            self._executor = ThreadPoolExecutor(max_workers=1)
        self._rate = rate
        self._frames_per_buffer = frames_per_buffer

    @property
    def rate(self):
        return self._rate

    def is_active(self):
        return self._pa and self._stream and self._stream.is_active()

    def start(self):
        if self._pa is None or self._stream is None:
          self._logger.error('AudioRecorder can only be used once!')
          return
        self._stream.start_stream()

    def read(self):
        if not self.is_active():
          return
        data = self._stream.read(self._frames_per_buffer)
        return np.fromstring(data, np.int16)

    async def async_read():
        if self._executor is None:
            return
        while stream.is_active():
          await self._executor.submit(self.read)

    def stop(self):
        self._stream.stop_stream()
        self._stream.close()
        self._pa.terminate()
        self._pa = None
        self._stream = None
