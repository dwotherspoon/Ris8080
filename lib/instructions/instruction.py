import random

class BasicBlock:
    def __init__(self):
        self._contents = []

    def add_item(self, item):
        self._contents.append(item)

    def get_assembly(self):
        return "\n".join([i.assemle() for i in self._contents])

    @property
    def size(self):
        return sum([i.size for i in self._contents])


# Interface for items in a block
class BlockItem:
    def assemble(self):
        raise NotImplementedError("Unimplemented assemble method")

    @property
    def size(self):
        raise NotImplementedError("Unimplemented size method")

# Instruction option types

class InstructionOption:
    def choose(self, state):
        raise NotImplementedError


class RegOption(InstructionOption):
    def __init__(self, choices, operation):
        self.choices = choices
        self.operation = operation

    def choose(self, state):
        return random.choice(self.choices)


class RegPairOption(InstructionOption):
    def __init__(self, choices, operation):
        self.choices = choices
        self.operation = operation

    def choose(self, state):
        return random.choice(self.choices)


class MemOption(InstructionOption):
    def __init__(self, choices, access_size, operation):
        pass

    def choose(self, state):
        return None


class MemPointer:
    def __init__(self, choices):
        pass


class ImmOption(InstructionOption):
    def __init__(self, imm_size):
        self.imm_size = imm_size

    def choose(self, state):
        return random.getrandbits(8 * self.imm_size)


class Instruction(BlockItem):
    _instr_registry = {}

    def __init__(self, options={}, state=None):
        self._options = options
        self.choices = {}
        for key, option in options.items():
            self.choices[key] = option.choose(state)

    # TODO: Consider moving registry to a parent class, e.g. generatoritem
    @classmethod
    def registry(cls):
        return cls._instr_registry

    def __init_subclass__(cls):
        assert cls.__name__ not in cls._instr_registry
        cls._instr_registry[cls.__name__] = cls


class OneByteInstruction(Instruction):
    @property
    def size(self):
        return 1


class TwoByteInstruction(Instruction):
    @property
    def size(self):
        return 2


class ThreeByteInstruction(Instruction):
    @property
    def size(self):
        return 3


class Label(BlockItem):
    def __init__(self, text):
        self._text = text

    def assemble(self):
        return self._text + ':'

    @property
    def size(self):
        return 0
