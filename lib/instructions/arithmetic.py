
from lib.instruction import OneByteInstruction, TwoByteInstruction

# Add register to accumulator
class ADD_Acc_Reg(OneByteInstruction):
    #options = InstructionOptionSet('source': InstructionRegisterOption)
    def assemble(self):
        return "add {0:s}".format(self.options['source'])

# Add memory to accumulator
class ADD_Acc_Mem(OneByteInstruction):
    def assemble(self):
        return "add M"

# Add immediate to accumulator
class ADI_Acc_Imm8(TwoByteInstruction):
    def assemble(self):
        return "adi {0:x}h".format(self.options['imm8'])

# Add register to accumulator with carry
class ADC_Acc_Reg(OneByteInstruction):
    def assemble(self):
        return "adc {0:s}".format(self.options['source'])

# Add memory to accumulator with carry
class ADC_Acc_Mem(OneByteInstruction):
    def assemble(self):
        return "adc M"

# Add immediate to accumulator with carry
class ACI_Acc_Imm8(TwoByteInstruction):
    def assemble(self):
        return "aci {0:x}h".format(self.options['imm8'])

# Add register pair to HL
class DAD_HL_RegPair(OneByteInstruction):
    def assemble(self):
        return "dad {0:s}".format(self.options['source'])

# Increment register
class INR_Reg(OneByteInstruction):
    def assemble(self):
        return "inr {0:s}".format(self.options['dest'])

# Increment memory
class INR_Mem(OneByteInstruction):
    def assemble(self):
        return "inr M"

# Decrement register
class DCR_Reg(OneByteInstruction):
    def assemble(self):
        return "dcr {0:s}".format(self.options['dest'])

# Decement memory
class DCR_Mem(OneByteInstruction):
    def assemble(self):
        return "dcr M"

# Increment register pair
class INX_RegPair(OneByteInstruction):
    def assemble(self):
        return "inx {0:s}".format(self.options['dest'])

# Decement register pair
class DCX_RegPair(OneByteInstruction):
    def assemble(self):
        return "dcx {0:s}".format(self.options['dest'])

# Subtract register from accumulator
class SUB_Acc_Reg(OneByteInstruction):
    def assemble(self):
        return "sub {0:s}".format(self.options['source'])

# Subtract memory from accumulator
class SUB_Acc_Mem(OneByteInstruction):
    def assemble(self):
        return "sub M"

# Subtract immediate from accumulator
class SUI_Acc_Imm(TwoByteInstruction):
    def assemble(self):
        return "sui {0:x}h".format(self.options['imm8'])

# Subtract register from accumulator with borrow
class SBB_Acc_Reg(OneByteInstruction):
    def assemble(self):
        return "sbb {0:s}".format(self.options['source'])

# Subtract memory from accumulator with borrow
class SBB_Acc_Mem(OneByteInstruction):
    def assemble(self):
        return "sbb M"

# Subtract immediate from accumulator with borrow
class SBI_Acc_Imm(TwoByteInstruction):
    def assemble(self):
        return "sbi {0:x}h".format(self.options['imm8'])

# Decimal adjust accumulator
class DAA_Acc(OneByteInstruction):
    def assemble(self):
        return "daa"
