
from lib.instructions.instruction import OneByteInstruction, TwoByteInstruction,RegOption, RegPairOption
from lib.register import Register, RegisterPair, Operation

# Add register to accumulator
class ADD_Acc_Reg(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'reg' : RegOption(choices=[Register.A, Register.B, Register.C, Register.D,
                                       Register.E, Register.H, Register.L],
                              operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "add {0:s}".format(self.choices['reg'])


# Add memory to accumulator
class ADD_Acc_Mem(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'mem' : MemOption(choices=[MemPointer(RegisterPair.HL)],
                              access_size=1,
                              operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "add M"


# Add immediate to accumulator
class ADI_Acc_Imm8(TwoByteInstruction):
    def __init__(self):
        options = {
            'acc'  : RegOption(choices=[Register.A],
                               operation=Operation.Read | Operation.Write),
            'imm8' : ImmOption(imm_size=1)
        }
        super().__init__(options)

    def assemble(self):
        return "adi {0:02x}h".format(self.choices['imm8'])


# Add register to accumulator with carry
class ADC_Acc_Reg(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'reg' : RegOption(choices=[Register.A, Register.B, Register.C, Register.D,
                                       Register.E, Register.H, Register.L],
                              operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "adc {0:s}".format(self.choices['reg'])


# Add memory to accumulator with carry
class ADC_Acc_Mem(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'mem' : MemOption(choices=[MemPointer(RegisterPair.HL)],
                              access_size=1,
                              operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "adc M"


# Add immediate to accumulator with carry
class ACI_Acc_Imm8(TwoByteInstruction):
    def __init__(self):
        options = {
            'acc'  : RegOption(choices=[Register.A],
                               operation=Operation.Read | Operation.Write),
            'imm8' : ImmOption(imm_size=1)
        }
        super().__init__(options)

    def assemble(self):
        return "aci {0:x}h".format(self.choices['imm8'])


# Add register pair to HL
class DAD_HL_RegPair(OneByteInstruction):
    def __init__(self):
        options = {
            'hl'   : RegPairOption(choices=[RegisterPair.HL],
                                   operation=Operation.Read | Operation.Write),
            'regp' : RegPairOption(choices=[RegisterPair.BC, RegisterPair.DE, RegisterPair.HL, RegisterPair.SP],
                                   operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "dad {0:s}".format(self.choices['regp'])


# Increment register
class INR_Reg(OneByteInstruction):
    def __init__(self):
        options = {
            'reg' : RegOption(choices=[Register.A, Register.B, Register.C, Register.D,
                                       Register.E, Register.H, Register.L],
                              operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "inr {0:s}".format(self.choices['reg'])


# Increment memory
class INR_Mem(OneByteInstruction):
    def __init__(self):
        options = {
            'mem' : MemOption(choices=[MemPointer(RegisterPair.HL)],
                              access_size=1,
                              operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "inr M"


# Decrement register
class DCR_Reg(OneByteInstruction):
    def __init__(self):
        options = {
            'reg' : RegOption(choices=[Register.A, Register.B, Register.C, Register.D,
                                       Register.E, Register.H, Register.L],
                              operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "dcr {0:s}".format(self.choices['reg'])


# Decement memory
class DCR_Mem(OneByteInstruction):
    def __init__(self):
        options = {
            'mem' : MemOption(choices=[MemPointer(RegisterPair.HL)],
                              access_size=1,
                              operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "dcr M"


# Increment register pair
class INX_RegPair(OneByteInstruction):
    def __init__(self):
        options = {
            'regp' : RegPairOption(choices=[RegisterPair.BC, RegisterPair.DE, RegisterPair.HL, RegisterPair.SP],
                                   operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "inx {0:s}".format(self.choices['regp'])


# Decement register pair
class DCX_RegPair(OneByteInstruction):
    def __init__(self):
        options = {
            'hl'   : RegPairOption(choices=[RegisterPair.HL],
                                   operation=Operation.Read | Operation.Write),
            'regp' : RegPairOption(choices=[RegisterPair.BC, RegisterPair.DE, RegisterPair.HL, RegisterPair.SP],
                                   operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "dcx {0:s}".format(self.choices['regp'])


# Subtract register from accumulator
class SUB_Acc_Reg(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'reg' : RegOption(choices=[Register.A, Register.B, Register.C, Register.D,
                                       Register.E, Register.H, Register.L],
                              operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "sub {0:s}".format(self.choices['reg'])


# Subtract memory from accumulator
class SUB_Acc_Mem(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'mem' : MemOption(choices=[MemPointer(RegisterPair.HL)],
                              access_size=1,
                              operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "sub M"


# Subtract immediate from accumulator
class SUI_Acc_Imm(TwoByteInstruction):
    def __init__(self):
        options = {
            'acc'  : RegOption(choices=[Register.A],
                               operation=Operation.Read | Operation.Write),
            'imm8' : ImmOption(imm_size=1)
        }
        super().__init__(options)

    def assemble(self):
        return "sui {0:x}h".format(self.choices['imm8'])


# Subtract register from accumulator with borrow
class SBB_Acc_Reg(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'reg' : RegOption(choices=[Register.A, Register.B, Register.C, Register.D,
                                       Register.E, Register.H, Register.L],
                              operation=Operation.Read | Operation.Write)
        }
        super().__init__(options)

    def assemble(self):
        return "sbb {0:s}".format(self.choices['reg'])


# Subtract memory from accumulator with borrow
class SBB_Acc_Mem(OneByteInstruction):
    def __init__(self):
        options = {
            'acc' : RegOption(choices=[Register.A],
                              operation=Operation.Read | Operation.Write),
            'mem' : MemOption(choices=[MemPointer(RegisterPair.HL)],
                              access_size=1,
                              operation=Operation.Read)
        }
        super().__init__(options)

    def assemble(self):
        return "sbb M"


# Subtract immediate from accumulator with borrow
class SBI_Acc_Imm(TwoByteInstruction):
    def __init__(self):
        options = {
            'acc'  : RegOption(choices=[Register.A],
                               operation=Operation.Read | Operation.Write),
            'imm8' : ImmOption(imm_size=1)
        }
        super().__init__(options)

    def assemble(self):
        return "sbi {0:x}h".format(self.choices['imm8'])


# Decimal adjust accumulator
class DAA_Acc(OneByteInstruction):
    def __init__(self):
        options = {
            'acc'  : RegOption(choices=[Register.A],
                               operation=Operation.Read | Operation.Write),
        }
        super().__init__(options)

    def assemble(self):
        return "daa"
