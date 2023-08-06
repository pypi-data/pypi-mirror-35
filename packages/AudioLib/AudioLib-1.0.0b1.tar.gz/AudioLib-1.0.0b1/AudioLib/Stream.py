# Author: Jacob Tsekrekos
# Date: June 29, 2018
# Description: A WaveForm Manager API
import threading
import time

from .WaveForm import WaveForm as _WaveForm
from ._pyaudio import PyAudio as _PyAudio
from ._pyaudio import get_format_from_width as _get_format

CHUNK_SIZE = 1024


class Stream:
    def __init__(self, filename, name=None):
        self.name = name
        self.loop = False
        self.__current = None
        self.__paused = False
        self.__playing = False
        self.__stopped = True

        # This may fail, Therefore self.__stream and self.waveform will not be defined
        self.__waveform = _WaveForm(filename).open()

        self.__stream = _PyAudio.open(
            format=_get_format(self.__waveform.sampleWidth),
            channels=self.__waveform.channels,
            rate=self.__waveform.framerate,
            output=True
        )

    def play(self):
        self.__current = threading.Thread(target=self.__play, name="Stream-Thread", daemon=True)
        self.__current.start()

    def __play(self):
        self.__playing = True
        while True:
            data = self.__waveform.read(CHUNK_SIZE)
            # Note that data is reading bytes so to be explicit, while data != b'':
            while data:
                if self.isPaused:
                    continue
                self.__stream.write(data)
                data = self.__waveform.read(CHUNK_SIZE)
            self.__waveform.position = 0 if not self.isPaused else self.__waveform.position
            if not self.loop:
                self.__playing = False
                exit()

    @property
    def isPaused(self):
        return self.__paused

    @property
    def isPlaying(self):
        return self.__playing

    @property
    def isStopped(self):
        return self.__stopped

    def pause(self):
        self.__paused = True

    def unPause(self):
        self.__paused = False

    def togglePause(self):
        self.__paused = not self.__paused

    def stop(self):
        self.__stopped = True

    def jumpTo(self, timeCode):
        pass

    @property
    def time(self):
        ":returns current time in seconds"
        return "{:.2f}".format(self.__waveform.position / self.__waveform.framerate)

    @property
    def totalTime(self):
        ":returns total time in seconds"
        return "{:.2f}".format(self.__waveform.frames / self.__waveform.framerate)

    def __del__(self):
        self.stop()


class Timer:
    def __init__(self):
        self.__timeThread = None
        self.startTime = 0
        self.current = 0

    def start(self):
        self.__timeThread = threading.Thread(target=self.__start, name="Timer", daemon=True)
        self.__timeThread.start()
        return self

    def __start(self):
        self.startTime = time.clock()
        while True:
            self.current = time.clock()

    def stop(self):
        self.__timeThread.exit()
        self.__timeThread = None

    @property
    def time(self):
        return round(self.current - self.startTime, 2)

    def __del__(self):
        if self.__timeThread:
            self.__timeThread.exit()


if __name__ == "__main__":
    s = Stream("test-piano.wav", "Piano")
    timer = Timer()
    s.play()
    s.loop = True
    while s.isPlaying:
        print(s.time)

    print("TOTAL:", s.totalTime)
