# Copyright (c) 2019 Xiaoyong Guo

import collections
import numpy as np

from .audio_recorder import AudioRecorder


def find_freq(samples):
    fft = np.fft.rfft(np.array(buf) * window)
    freq = (np.abs(fft[imin:imax]).argmax() + imin) * FREQ_STEP


class ETuner(object):
    def __init__(self):
        self._audio_recorder = AudioRecorder()
        rate = self._audio_recorder.rate
        self._buffer_size = rate
        self._buffer = collections.deque(maxlen=self._buffer_size)
        self._freq = None

    def start(self):
        while self._audio_recorder.is_active():
            data = self._audio_recorder.read()
            self._buffer.extend(data)
            print(len(data))
            if len(self._buffer) < self._buffer_size:
                continue
            #data = np.array()
            #freq = find_freq(data)

    def stop(self):
        self._audio_recorder.stop()


def main():
    etuner = ETuner()
    try:
        etuner.start()
    except KeyboardInterrupt:
        etuner.stop()


if __name__ == '__main__':
    main()
