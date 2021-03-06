from enum import IntEnum, IntFlag

class Register(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    H = 5
    L = 6


class RegisterPair(IntEnum):
    BC = 0
    DE = 1
    HL = 2
    SP = 3


class Operation(IntFlag):
    Read  = 1
    Write = 2
