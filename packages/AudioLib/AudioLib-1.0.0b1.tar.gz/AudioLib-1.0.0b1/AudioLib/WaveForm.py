# Author: Jacob Tsekrekos
# Date: June 29, 2018
# Description: A WaveForm Manager API

import aifc
import wave


# https://docs.python.org/3/library/aifc.html
# https://docs.python.org/3/library/wave.html
# AIFF is currently broken: Problem with the library loading?


class AudioFormat:
    def __init__(self, magicNumber, extension):
        self.magicNumber = magicNumber
        self.extension = extension

    def __eq__(self, other):
        if not isinstance(other, AudioFormat):
            return False

        if other.magicNumber == self.magicNumber:
            return True
        else:
            return False


class FormatError(Exception):
    pass


WAV = AudioFormat([82, 73, 70, 70, -1, -1, -1, -1, 87, 65, 86, 69], "wav")
AIFF = AudioFormat([70, 79, 82, 77, -1, -1, -1, -1, 65, 73, 70, 70], "aiff")

supportedFormats = [WAV, AIFF]


def bytesEqual(check, array):
    for i, j in enumerate(array):
        # accounts for wildcards
        if check[i] == -1 or array[i] == -1:
            continue

        if array[i] != check[i]:
            return False

    return True


class WaveForm:
    def __init__(self, filename):
        self.filename = filename
        self.fileFormat = None
        self.file = None

        error = None
        try:
            open(filename, "rb").close()
        except FileNotFoundError:
            error = FileNotFoundError
        if error:
            raise FileNotFoundError

        with open(filename, "rb") as file:
            magicNumber = file.read(12)

        for check in supportedFormats:
            if bytesEqual(check.magicNumber, magicNumber):
                self.fileFormat = check
                break

        if self.fileFormat is WAV:
            self.__codec = wave

        elif self.fileFormat is AIFF:
            self.__codec = aifc
        else:
            message = "Magic number is not recognized, format not supported."
            raise FormatError(message)

        # ensures all constants are set
        self.open()
        self.framerate = self.file.getframerate()
        self.frames = self.file.getnframes()
        self.channels = self.file.getnchannels()
        self.sampleWidth = self.file.getsampwidth()
        self.close()

    def open(self):
        self.file = self.__codec.open(self.filename)
        return self

    def close(self):
        if self.isOpen:
            self.file.close()
            self.file = None
        return self

    def read(self, n):
        if self.isOpen:
            return self.file.readframes(n)

    @property
    def isOpen(self):
        return True if self.file is not None else False

    @property
    def position(self):
        return self.file.tell()

    @position.setter
    def position(self, new):
        self.file.setpos(new)


        # s = WaveForm("hello", "test-piano.wav")
        # s.open()
        # print(s.isOpen)
        # print(s.channels)
        # print(s.position)
        # s.position = 100
        # print(s.position)
