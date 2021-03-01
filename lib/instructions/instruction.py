class BasicBlock:
    def __init__(self):
        self._contents = []
    
    def add_item(self, item):
        self._contents.append(item)
    
    def get_assembly(self):
        return "\n".join([i.assemle() for i in in self._contents])
    
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

class InstructionOptions:
    pass

class InstructionOptionSet:
    pass

class Instruction(BlockItem):
    def __init__(self, options):
        self._options = options

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