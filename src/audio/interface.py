class abs_WaveFile:
    def __init__(self, file):
        self._file = file

    def get_file(self):
        return self._file

class abs_AudioOut:
    _name = 'abs_AudioOut'
    _playing = False

    _file:abs_WaveFile

    def __init__(self, pin):
        self._pin = pin

    def play(self, file:abs_WaveFile):
        self._file = file._file
        self._log("play", "started play")
        self._playing = True

    def deinit(self):
        message = "stopped" if self._playing else "deinit"
        self._log("deinit", message)

    def _log(self, method:str, message:any):
        print("["+self._pin+"] "+self._name+":"+method+":"+str(message))

