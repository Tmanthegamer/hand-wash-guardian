from . import abs_WaveFile
from . import abs_AudioOut

import winsound

class WaveFile(abs_WaveFile):


    def __init__(self, file):
        super().__init__(file)


class AudioOut(abs_AudioOut):
    _name = 'windows_audio_out'

    def __init__(self, pin):
        super().__init__(pin)

    def play(self, file: abs_WaveFile):
        super().play(file)

        filePath = file.get_file().name
        winsound.PlaySound(filePath, winsound.SND_FILENAME)

    def deinit(self):
        super().deinit()
