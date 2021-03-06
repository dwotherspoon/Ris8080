
from lib.instructions.arithmetic import *
from lib.instructions.data import *
from lib.instructions.instruction import Instruction

# A bag like structure for weighted choice of GeneratorItems
class GeneratorItemBag:
    def get_item(self):
        pass

class StreamGenerator:
    def __init__(self, state):
        self._state = state
    
    def generate(self):
        print(Instruction.registry())
        for _ in range(0, 1000):
            item = self._state.choose_item()
            print(item(self._state).assemble()) 