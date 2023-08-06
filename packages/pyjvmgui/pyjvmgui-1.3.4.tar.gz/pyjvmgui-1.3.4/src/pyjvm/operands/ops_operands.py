
from pyjvm.bytecode import operands
import logging
import struct

logger = logging.getLogger(__name__)


def unpack_byte(bin_str):
    return struct.unpack(">b", bin_str)[0]

def unpack_short(bin_str):
    return struct.unpack(">h", bin_str)[0]

def unpack_int(bin_str):
    return struct.unpack(">i", bin_str)[0]

@operands(code=0x19)
def aload(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x3a)
def astore(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x10)
def bipush(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x18)
def dload(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x39)
def dstore(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x17)
def fload(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x38)
def fstore(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x15)
def iload(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x36)
def istore(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x12)
def ldc(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x16)
def lload(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x37)
def lstore(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xbc)
def newarray(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa9)
def ret(frame):
    division_arr = [1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xbd)
def anewarray(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc0)
def checkcast(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb4)
def getfield(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb2)
def getstatic(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa7)
def goto(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa5)
def if_acmpeq(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa6)
def if_acmpne(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x9f)
def if_icmpeq(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa2)
def if_icmpge(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa3)
def if_icmpgt(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa4)
def if_icmple(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa1)
def if_icmplt(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa0)
def if_icmpne(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x99)
def ifeq(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x9c)
def ifge(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x9d)
def ifgt(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x9e)
def ifle(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x9b)
def iflt(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x9a)
def ifne(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc7)
def ifnonnull(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc6)
def ifnull(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x84)
def iinc(frame):
    division_arr = [1, 1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc1)
def instanceof(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb7)
def invokespecial(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb8)
def invokestatic(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb6)
def invokevirtual(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xa8)
def jsr(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x13)
def ldc_w(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x14)
def ldc2_w(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xbb)
def new(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb5)
def putfield(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb3)
def putstatic(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0x11)
def sipush(frame):
    division_arr = [2] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc5)
def multianewarray(frame):
    division_arr = [2, 1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc8)
def goto_w(frame):
    division_arr = [4] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xba)
def invokedynamic(frame):
    division_arr = [2, 1, 1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xb9)
def invokeinterface(frame):
    division_arr = [2, 1, 1] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xc9)
def jsr_w(frame):
    division_arr = [4] 
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = frame.code[frame.pc + offset : frame.pc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    return operands

@operands(code=0xaa)
def tableswitch(frame):
    logger.warn("tableswitch operands not supported")
    return []

@operands(code=0xc4)
def wide(frame):
    logger.warn("wide operands not supported")
    return []

@operands(code=0xab)
def lookupswitch(frame):
    logger.warn("lookupswitch operands not supported")
    return []

@operands(code=0x32)
def aaload(frame):
    return []

@operands(code=0x53)
def aastore(frame):
    return []

@operands(code=0x1)
def aconst_null(frame):
    return []

@operands(code=0x2a)
def aload_0(frame):
    return []

@operands(code=0x2b)
def aload_1(frame):
    return []

@operands(code=0x2c)
def aload_2(frame):
    return []

@operands(code=0x2d)
def aload_3(frame):
    return []

@operands(code=0xb0)
def areturn(frame):
    return []

@operands(code=0xbe)
def arraylength(frame):
    return []

@operands(code=0x4b)
def astore_0(frame):
    return []

@operands(code=0x4c)
def astore_1(frame):
    return []

@operands(code=0x4d)
def astore_2(frame):
    return []

@operands(code=0x4e)
def astore_3(frame):
    return []

@operands(code=0xbf)
def athrow(frame):
    return []

@operands(code=0x33)
def baload(frame):
    return []

@operands(code=0x54)
def bastore(frame):
    return []

@operands(code=0xca)
def breakpoint(frame):
    return []

@operands(code=0x34)
def caload(frame):
    return []

@operands(code=0x55)
def castore(frame):
    return []

@operands(code=0x90)
def d2f(frame):
    return []

@operands(code=0x8e)
def d2i(frame):
    return []

@operands(code=0x8f)
def d2l(frame):
    return []

@operands(code=0x63)
def dadd(frame):
    return []

@operands(code=0x31)
def daload(frame):
    return []

@operands(code=0x52)
def dastore(frame):
    return []

@operands(code=0x98)
def dcmpg(frame):
    return []

@operands(code=0x97)
def dcmpl(frame):
    return []

@operands(code=0x0e)
def dconst_0(frame):
    return []

@operands(code=0x0f)
def dconst_1(frame):
    return []

@operands(code=0x6f)
def ddiv(frame):
    return []

@operands(code=0x26)
def dload_0(frame):
    return []

@operands(code=0x27)
def dload_1(frame):
    return []

@operands(code=0x28)
def dload_2(frame):
    return []

@operands(code=0x29)
def dload_3(frame):
    return []

@operands(code=0x6b)
def dmul(frame):
    return []

@operands(code=0x77)
def dneg(frame):
    return []

@operands(code=0x73)
def drem(frame):
    return []

@operands(code=0xaf)
def dreturn(frame):
    return []

@operands(code=0x47)
def dstore_0(frame):
    return []

@operands(code=0x48)
def dstore_1(frame):
    return []

@operands(code=0x49)
def dstore_2(frame):
    return []

@operands(code=0x4a)
def dstore_3(frame):
    return []

@operands(code=0x67)
def dsub(frame):
    return []

@operands(code=0x59)
def dup(frame):
    return []

@operands(code=0x5a)
def dup_x1(frame):
    return []

@operands(code=0x5b)
def dup_x2(frame):
    return []

@operands(code=0x5c)
def dup2(frame):
    return []

@operands(code=0x5d)
def dup2_x1(frame):
    return []

@operands(code=0x5e)
def dup2_x2(frame):
    return []

@operands(code=0x8d)
def f2d(frame):
    return []

@operands(code=0x8b)
def f2i(frame):
    return []

@operands(code=0x8c)
def f2l(frame):
    return []

@operands(code=0x62)
def fadd(frame):
    return []

@operands(code=0x30)
def faload(frame):
    return []

@operands(code=0x51)
def fastore(frame):
    return []

@operands(code=0x96)
def fcmpg(frame):
    return []

@operands(code=0x95)
def fcmpl(frame):
    return []

@operands(code=0x0b)
def fconst_0(frame):
    return []

@operands(code=0x0c)
def fconst_1(frame):
    return []

@operands(code=0x0d)
def fconst_2(frame):
    return []

@operands(code=0x6e)
def fdiv(frame):
    return []

@operands(code=0x22)
def fload_0(frame):
    return []

@operands(code=0x23)
def fload_1(frame):
    return []

@operands(code=0x24)
def fload_2(frame):
    return []

@operands(code=0x25)
def fload_3(frame):
    return []

@operands(code=0x6a)
def fmul(frame):
    return []

@operands(code=0x76)
def fneg(frame):
    return []

@operands(code=0x72)
def frem(frame):
    return []

@operands(code=0xae)
def freturn(frame):
    return []

@operands(code=0x43)
def fstore_0(frame):
    return []

@operands(code=0x44)
def fstore_1(frame):
    return []

@operands(code=0x45)
def fstore_2(frame):
    return []

@operands(code=0x46)
def fstore_3(frame):
    return []

@operands(code=0x66)
def fsub(frame):
    return []

@operands(code=0x91)
def i2b(frame):
    return []

@operands(code=0x92)
def i2c(frame):
    return []

@operands(code=0x87)
def i2d(frame):
    return []

@operands(code=0x86)
def i2f(frame):
    return []

@operands(code=0x85)
def i2l(frame):
    return []

@operands(code=0x93)
def i2s(frame):
    return []

@operands(code=0x60)
def iadd(frame):
    return []

@operands(code=0x2e)
def iaload(frame):
    return []

@operands(code=0x7e)
def iand(frame):
    return []

@operands(code=0x4f)
def iastore(frame):
    return []

@operands(code=0x2)
def iconst_m1(frame):
    return []

@operands(code=0x3)
def iconst_0(frame):
    return []

@operands(code=0x4)
def iconst_1(frame):
    return []

@operands(code=0x5)
def iconst_2(frame):
    return []

@operands(code=0x6)
def iconst_3(frame):
    return []

@operands(code=0x7)
def iconst_4(frame):
    return []

@operands(code=0x8)
def iconst_5(frame):
    return []

@operands(code=0x6c)
def idiv(frame):
    return []

@operands(code=0x1a)
def iload_0(frame):
    return []

@operands(code=0x1b)
def iload_1(frame):
    return []

@operands(code=0x1c)
def iload_2(frame):
    return []

@operands(code=0x1d)
def iload_3(frame):
    return []

@operands(code=0xfe)
def impdep1(frame):
    return []

@operands(code=0xff)
def impdep2(frame):
    return []

@operands(code=0x68)
def imul(frame):
    return []

@operands(code=0x74)
def ineg(frame):
    return []

@operands(code=0x80)
def ior(frame):
    return []

@operands(code=0x70)
def irem(frame):
    return []

@operands(code=0xac)
def ireturn(frame):
    return []

@operands(code=0x78)
def ishl(frame):
    return []

@operands(code=0x7a)
def ishr(frame):
    return []

@operands(code=0x3b)
def istore_0(frame):
    return []

@operands(code=0x3c)
def istore_1(frame):
    return []

@operands(code=0x3d)
def istore_2(frame):
    return []

@operands(code=0x3e)
def istore_3(frame):
    return []

@operands(code=0x64)
def isub(frame):
    return []

@operands(code=0x7c)
def iushr(frame):
    return []

@operands(code=0x82)
def ixor(frame):
    return []

@operands(code=0x8a)
def l2d(frame):
    return []

@operands(code=0x89)
def l2f(frame):
    return []

@operands(code=0x88)
def l2i(frame):
    return []

@operands(code=0x61)
def ladd(frame):
    return []

@operands(code=0x2f)
def laload(frame):
    return []

@operands(code=0x7f)
def land(frame):
    return []

@operands(code=0x50)
def lastore(frame):
    return []

@operands(code=0x94)
def lcmp(frame):
    return []

@operands(code=0x9)
def lconst_0(frame):
    return []

@operands(code=0x0a)
def lconst_1(frame):
    return []

@operands(code=0x6d)
def ldiv(frame):
    return []

@operands(code=0x1e)
def lload_0(frame):
    return []

@operands(code=0x1f)
def lload_1(frame):
    return []

@operands(code=0x20)
def lload_2(frame):
    return []

@operands(code=0x21)
def lload_3(frame):
    return []

@operands(code=0x69)
def lmul(frame):
    return []

@operands(code=0x75)
def lneg(frame):
    return []

@operands(code=0x81)
def lor(frame):
    return []

@operands(code=0x71)
def lrem(frame):
    return []

@operands(code=0xad)
def lreturn(frame):
    return []

@operands(code=0x79)
def lshl(frame):
    return []

@operands(code=0x7b)
def lshr(frame):
    return []

@operands(code=0x3f)
def lstore_0(frame):
    return []

@operands(code=0x40)
def lstore_1(frame):
    return []

@operands(code=0x41)
def lstore_2(frame):
    return []

@operands(code=0x42)
def lstore_3(frame):
    return []

@operands(code=0x65)
def lsub(frame):
    return []

@operands(code=0x7d)
def lushr(frame):
    return []

@operands(code=0x83)
def lxor(frame):
    return []

@operands(code=0xc2)
def monitorenter(frame):
    return []

@operands(code=0xc3)
def monitorexit(frame):
    return []

@operands(code=0x0)
def nop(frame):
    return []

@operands(code=0x57)
def pop(frame):
    return []

@operands(code=0x58)
def pop2(frame):
    return []

@operands(code=0xb1)
def return_(frame):
    return []

@operands(code=0x35)
def saload(frame):
    return []

@operands(code=0x56)
def sastore(frame):
    return []

@operands(code=0x5f)
def swap(frame):
    return []
