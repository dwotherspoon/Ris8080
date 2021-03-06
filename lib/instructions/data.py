
from lib.instructions.instruction import OneByteInstruction, TwoByteInstruction, ThreeByteInstruction

# Move immediate into register
class MVI_Reg_Imm8(TwoByteInstruction):
    pass

# Move immediate into memory
class MVI_Mem_Imm8(TwoByteInstruction):
    pass

# Move register into register
class MOV_Reg_reg(OneByteInstruction):
    pass

# Move register into memory
class MOV_Mem_Reg(OneByteInstruction):
    pass

# Move memory into register
class MOV_Reg_Mem(OneByteInstruction):
    pass

# Load immediate register pair
class LXI_RegPair_Imm16(ThreeByteInstruction):
    pass

# Store accumulator indirect (reg pair BC or DE)
class STAX_RegPair(OneByteInstruction):
    pass

# Load accumulator indirect (reg pair BC or DE)
class LDAX_RegPair(OneByteInstruction):
    pass

# Load accumulator direct
class LDA_Imm16(ThreeByteInstruction):
    pass

# Store accumulator direct
class STA_Imm16(ThreeByteInstruction):
    pass

# Load HL direct
class LHLD_Imm16(ThreeByteInstruction):
    pass

# Store HL direct
class SHLD_Imm16(ThreeByteInstruction):
    pass

# Exchange DE with HL
class XCHG(OneByteInstruction):
    pass