class custom_adapter:
    def __init__(self, source=None):
        self.__source = source

    def get(self, key:str):
        if(source is None):
            return self._value
        type(source)

    def set(self, value):
        self._value = value
        return self

class abs_io_device:
    _direction = custom_adapter()
    _pull = custom_adapter()
    _name = 'abs_io_device'
    _value = None

    def __init__(self, pin):
        self._pin = pin

    def set_direction(self, value):
        self._direction.set(value)
        return self

    def set_pull(self, value):
        self._pull.set(value)
        return self

    def set_value(self, value):
        self._value = value
        return self

    def get_value(self):
        return self._value

    def _log(self, method: str, message: any):
        print("["+str(self._pin)+"] "+self._name+":"+method+":"+str(message))

class abs_digital_io:
    def __init__(self):
        pass

    def DigitalInOut(self, pin: any):
        return abs_digital_io(pin)
