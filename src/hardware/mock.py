from . import abs_io_device
from . import constants


class io_device(abs_io_device):
    _name = 'mock_io_device'

    def __init__(self, pin):
        super().__init__(pin)

    def set_direction(self, value):
        self._log("set_direction", value);
        return super().set_direction(value)

    def set_pull(self, value):
        self._log("set_pull", value)
        return super().set_pull(value)

    def set_value(self, value):
        self._log("set_value", value)
        return super().set_value(value)

class digitial_io:
    def __init__(self):
        self.Direction = constants.Direction
        self.Pull = constants.Pull

    def DigitalInOut(self, pin: any):
        return io_device(pin)
