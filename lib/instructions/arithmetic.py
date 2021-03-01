
from lib.instruction import OneByteInstruction, TwoByteInstruction

# Add register to accumulator
class ADD_Acc_Reg(OneByteInstruction):
    #options = InstructionOptionSet('source': InstructionRegisterOption)
    pass

# Add memory to accumulator
class ADD_Acc_Mem(OneByteInstruction):
    pass

# Add immediate to accumulator
class ADI_Acc_Imm(TwoByteInstruction):
    pass

# Add register to accumulator with carry
class ADC_Acc_Reg(OneByteInstruction):
    pass

# Add memory to accumulator with carry
class ADC_Acc_Mem(OneByteInstruction):
    pass

# Add immediate to accumulator with carry
class ACI_Acc_Imm(TwoByteInstruction):
    pass

# Add register pair to HL
class DAD_HL_RegPair(OneByteInstruction):
    pass

# Increment register
class INR_Reg(OneByteInstruction):
    pass

# Increment memory
class INR_Mem(OneByteInstruction):
    pass

# Decrement register
class DCR_Reg(OneByteInstruction):
    pass

# Decement memory
class DCR_Mem(OneByteInstruction):
    pass

# Increment register pair
class INX_RegPair(OneByteInstruction):
    pass

# Decement register pair
class DCX_RegPair(OneByteInstruction):
    pass

# Subtract register from accumulator
class SUB_Acc_Reg(OneByteInstruction):
    pass

# Subtract memory from accumulator
class SUB_Acc_Mem(OneByteInstruction):
    pass

# Subtract immediate from accumulator
class SUI_Acc_Imm(TwoByteInstruction):
    pass

# Subtract register from accumulator with borrow
class SBB_Acc_Reg(OneByteInstruction):
    pass

# Subtract memory from accumulator with borrow
class SBB_Acc_Mem(OneByteInstruction):
    pass

# Subtract immediate from accumulator with borrow
class SBI_Acc_Imm(TwoByteInstruction):
    pass

# Decimal adjust accumulator
class DAA_Acc(OneByteInstruction):
    pass
