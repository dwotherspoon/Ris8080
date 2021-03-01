class RegisterState:
    @property
    def readable(self):
        raise NotImplementedError

    @property
    def writable(self):
        raise NotImplementedError

class SingleRegisterState(RegisterState):
    def __init__(self):
        self._readable = True
        self._writable = True
    
    def make_unreadable(self):
        assert self._readable
        self._readable = False
    
    def make_unwritable(self):
        assert self._writable
        self._writable = False
    
    @property
    def readable(self):
        return self._readable

    @property
    def writable(self):
        return self._writable

class RegisterPairState(RegisterState):
    def __init__(self, high, low):
        self._low = low
        self._high = high
    
    @property
    def readable(self):
        return self._low.readable and self._high.readable
    
    @property
    def writable(self):
        return self._low.writable and self._high.writable

class SPRegisterState(SingleRegisterState):
    def __init__(self, value):
        self._value = value
    # TODO: Define operations to modify value

class State:
    def __init__(self, config):
        self._config = config
        self._registers = {
            'A' : SingleRegisterState(),
            'B' : SingleRegisterState(),
            'C' : SingleRegisterState(),
            'D' : SingleRegisterState(),
            'E' : SingleRegisterState(),
            'H' : SingleRegisterState(),
            'L' : SingleRegisterState()
        }

        self._register_pairs = {
            'BC' : RegisterPairState(self._registers['B'], self._registers['C']),
            'DE' : RegisterPairState(self._registers['D'], self._registers['E']),
            'HL' : RegisterPairState(self._registers['H'], self._registers['L']),
            # Technically not a true register pair
            'SP' : SPRegisterState(config.sp_initial)
        }