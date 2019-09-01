# Copyright (c) 2019 Xiaoyong Guo

import collections
import numpy as np

from .audio_recorder import AudioRecorder


def find_freq(sound_samples, rate):
    n = int(2 ** np.ceil(np.log2(len(sound_samples))))
    fft = np.fft.rfft(sound_samples, n)
    fft_abs = np.abs(fft)
    if np.max(fft_abs) < 50000:
        freq = None
    else:
        freq = np.argmax(fft_abs) * rate / n
    return freq


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
            if len(self._buffer) < self._buffer_size:
                continue
            sound_samples = np.array(self._buffer)
            freq = find_freq(data, self._audio_recorder.rate)
            if freq is not None:
                print(freq)

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
