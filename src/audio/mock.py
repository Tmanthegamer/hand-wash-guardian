from . import abs_WaveFile
from . import abs_AudioOut

class WaveFile(abs_WaveFile):

    def __init__(self, file):
        super().__init__(file)


class AudioOut(abs_AudioOut):
    _name = 'mock_audio_out'

    def __init__(self, pin):
        super().__init__(pin)
