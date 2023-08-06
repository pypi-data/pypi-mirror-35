
from pyjvm.bytecode import to_bytecode
from gui.abstractions.bytecode import Bytecode
import logging
import struct

logger = logging.getLogger(__name__)


def unpack_byte(bin_str):
    return struct.unpack(">b", bin_str)[0]

def unpack_short(bin_str):
    return struct.unpack(">h", bin_str)[0]

def unpack_int(bin_str):
    return struct.unpack(">i", bin_str)[0]

@to_bytecode(code=0x19)
def aload(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x19, operands)) 

@to_bytecode(code=0x3a)
def astore(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x3a, operands)) 

@to_bytecode(code=0x10)
def bipush(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x10, operands)) 

@to_bytecode(code=0x18)
def dload(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x18, operands)) 

@to_bytecode(code=0x39)
def dstore(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x39, operands)) 

@to_bytecode(code=0x17)
def fload(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x17, operands)) 

@to_bytecode(code=0x38)
def fstore(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x38, operands)) 

@to_bytecode(code=0x15)
def iload(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x15, operands)) 

@to_bytecode(code=0x36)
def istore(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x36, operands)) 

@to_bytecode(code=0x12)
def ldc(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x12, operands)) 

@to_bytecode(code=0x16)
def lload(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x16, operands)) 

@to_bytecode(code=0x37)
def lstore(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0x37, operands)) 

@to_bytecode(code=0xbc)
def newarray(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0xbc, operands)) 

@to_bytecode(code=0xa9)
def ret(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 1, Bytecode(loc, 0xa9, operands)) 

@to_bytecode(code=0xbd)
def anewarray(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xbd, operands)) 

@to_bytecode(code=0xc0)
def checkcast(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xc0, operands)) 

@to_bytecode(code=0xb4)
def getfield(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb4, operands)) 

@to_bytecode(code=0xb2)
def getstatic(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb2, operands)) 

@to_bytecode(code=0xa7)
def goto(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa7, operands)) 

@to_bytecode(code=0xa5)
def if_acmpeq(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa5, operands)) 

@to_bytecode(code=0xa6)
def if_acmpne(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa6, operands)) 

@to_bytecode(code=0x9f)
def if_icmpeq(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x9f, operands)) 

@to_bytecode(code=0xa2)
def if_icmpge(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa2, operands)) 

@to_bytecode(code=0xa3)
def if_icmpgt(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa3, operands)) 

@to_bytecode(code=0xa4)
def if_icmple(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa4, operands)) 

@to_bytecode(code=0xa1)
def if_icmplt(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa1, operands)) 

@to_bytecode(code=0xa0)
def if_icmpne(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa0, operands)) 

@to_bytecode(code=0x99)
def ifeq(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x99, operands)) 

@to_bytecode(code=0x9c)
def ifge(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x9c, operands)) 

@to_bytecode(code=0x9d)
def ifgt(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x9d, operands)) 

@to_bytecode(code=0x9e)
def ifle(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x9e, operands)) 

@to_bytecode(code=0x9b)
def iflt(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x9b, operands)) 

@to_bytecode(code=0x9a)
def ifne(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x9a, operands)) 

@to_bytecode(code=0xc7)
def ifnonnull(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xc7, operands)) 

@to_bytecode(code=0xc6)
def ifnull(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xc6, operands)) 

@to_bytecode(code=0x84)
def iinc(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [1, 1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x84, operands)) 

@to_bytecode(code=0xc1)
def instanceof(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xc1, operands)) 

@to_bytecode(code=0xb7)
def invokespecial(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb7, operands)) 

@to_bytecode(code=0xb8)
def invokestatic(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb8, operands)) 

@to_bytecode(code=0xb6)
def invokevirtual(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb6, operands)) 

@to_bytecode(code=0xa8)
def jsr(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xa8, operands)) 

@to_bytecode(code=0x13)
def ldc_w(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x13, operands)) 

@to_bytecode(code=0x14)
def ldc2_w(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x14, operands)) 

@to_bytecode(code=0xbb)
def new(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xbb, operands)) 

@to_bytecode(code=0xb5)
def putfield(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb5, operands)) 

@to_bytecode(code=0xb3)
def putstatic(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0xb3, operands)) 

@to_bytecode(code=0x11)
def sipush(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 2, Bytecode(loc, 0x11, operands)) 

@to_bytecode(code=0xc5)
def multianewarray(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2, 1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 3, Bytecode(loc, 0xc5, operands)) 

@to_bytecode(code=0xc8)
def goto_w(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [4]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 4, Bytecode(loc, 0xc8, operands)) 

@to_bytecode(code=0xba)
def invokedynamic(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2, 1, 1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 4, Bytecode(loc, 0xba, operands)) 

@to_bytecode(code=0xb9)
def invokeinterface(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [2, 1, 1]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 4, Bytecode(loc, 0xb9, operands)) 

@to_bytecode(code=0xc9)
def jsr_w(loc, code):
    """
    :return (size, Bytecode)
    """
    division_arr = [4]
    operands = []
    offset = 1
    for op in division_arr:
        cur_op_slice = code[loc + offset : loc + offset + op]
        if op == 1:
            operands.append(unpack_byte(cur_op_slice))
        elif op == 2:
            operands.append(unpack_short(cur_op_slice))
        elif op == 4:
            operands.append(unpack_int(cur_op_slice))
        offset += op
    
    return (1 + 4, Bytecode(loc, 0xc9, operands)) 

@to_bytecode(code=0xaa)
def tableswitch(code):
    logger.warn("tableswitch operands not supported")
    return []

@to_bytecode(code=0xc4)
def wide(code):
    logger.warn("wide operands not supported")
    return []

@to_bytecode(code=0xab)
def lookupswitch(loc, code):
    """
    https://cs.au.dk/~mis/dOvs/jvmspec/ref--41.html
    :return:
    """
    loc_offset = loc + 1
    operands = []
    while loc_offset % 4 != 0:
        loc_offset += 1

    default_offset = unpack_int(code[loc_offset: loc_offset + 4])
    loc_offset += 4
    operands.append(default_offset)

    n = unpack_int(code[loc_offset: loc_offset + 4])
    loc_offset += 4
    operands.append(n)

    for i in range(n):
        key = unpack_int(code[loc_offset: loc_offset + 4])
        loc_offset += 4
        operands.append(key)
        offset = unpack_int(code[loc_offset: loc_offset + 4])
        loc_offset += 4
        operands.append(offset)
        
    return (loc_offset - loc, Bytecode(loc, 0xab, operands))

@to_bytecode(code=0x32)
def aaload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x32, []))
    
@to_bytecode(code=0x53)
def aastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x53, []))
    
@to_bytecode(code=0x1)
def aconst_null(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1, []))
    
@to_bytecode(code=0x2a)
def aload_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2a, []))
    
@to_bytecode(code=0x2b)
def aload_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2b, []))
    
@to_bytecode(code=0x2c)
def aload_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2c, []))
    
@to_bytecode(code=0x2d)
def aload_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2d, []))
    
@to_bytecode(code=0xb0)
def areturn(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xb0, []))
    
@to_bytecode(code=0xbe)
def arraylength(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xbe, []))
    
@to_bytecode(code=0x4b)
def astore_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4b, []))
    
@to_bytecode(code=0x4c)
def astore_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4c, []))
    
@to_bytecode(code=0x4d)
def astore_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4d, []))
    
@to_bytecode(code=0x4e)
def astore_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4e, []))
    
@to_bytecode(code=0xbf)
def athrow(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xbf, []))
    
@to_bytecode(code=0x33)
def baload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x33, []))
    
@to_bytecode(code=0x54)
def bastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x54, []))
    
@to_bytecode(code=0xca)
def breakpoint(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xca, []))
    
@to_bytecode(code=0x34)
def caload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x34, []))
    
@to_bytecode(code=0x55)
def castore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x55, []))
    
@to_bytecode(code=0x90)
def d2f(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x90, []))
    
@to_bytecode(code=0x8e)
def d2i(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8e, []))
    
@to_bytecode(code=0x8f)
def d2l(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8f, []))
    
@to_bytecode(code=0x63)
def dadd(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x63, []))
    
@to_bytecode(code=0x31)
def daload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x31, []))
    
@to_bytecode(code=0x52)
def dastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x52, []))
    
@to_bytecode(code=0x98)
def dcmpg(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x98, []))
    
@to_bytecode(code=0x97)
def dcmpl(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x97, []))
    
@to_bytecode(code=0x0e)
def dconst_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0e, []))
    
@to_bytecode(code=0x0f)
def dconst_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0f, []))
    
@to_bytecode(code=0x6f)
def ddiv(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6f, []))
    
@to_bytecode(code=0x26)
def dload_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x26, []))
    
@to_bytecode(code=0x27)
def dload_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x27, []))
    
@to_bytecode(code=0x28)
def dload_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x28, []))
    
@to_bytecode(code=0x29)
def dload_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x29, []))
    
@to_bytecode(code=0x6b)
def dmul(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6b, []))
    
@to_bytecode(code=0x77)
def dneg(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x77, []))
    
@to_bytecode(code=0x73)
def drem(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x73, []))
    
@to_bytecode(code=0xaf)
def dreturn(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xaf, []))
    
@to_bytecode(code=0x47)
def dstore_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x47, []))
    
@to_bytecode(code=0x48)
def dstore_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x48, []))
    
@to_bytecode(code=0x49)
def dstore_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x49, []))
    
@to_bytecode(code=0x4a)
def dstore_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4a, []))
    
@to_bytecode(code=0x67)
def dsub(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x67, []))
    
@to_bytecode(code=0x59)
def dup(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x59, []))
    
@to_bytecode(code=0x5a)
def dup_x1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5a, []))
    
@to_bytecode(code=0x5b)
def dup_x2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5b, []))
    
@to_bytecode(code=0x5c)
def dup2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5c, []))
    
@to_bytecode(code=0x5d)
def dup2_x1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5d, []))
    
@to_bytecode(code=0x5e)
def dup2_x2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5e, []))
    
@to_bytecode(code=0x8d)
def f2d(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8d, []))
    
@to_bytecode(code=0x8b)
def f2i(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8b, []))
    
@to_bytecode(code=0x8c)
def f2l(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8c, []))
    
@to_bytecode(code=0x62)
def fadd(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x62, []))
    
@to_bytecode(code=0x30)
def faload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x30, []))
    
@to_bytecode(code=0x51)
def fastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x51, []))
    
@to_bytecode(code=0x96)
def fcmpg(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x96, []))
    
@to_bytecode(code=0x95)
def fcmpl(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x95, []))
    
@to_bytecode(code=0x0b)
def fconst_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0b, []))
    
@to_bytecode(code=0x0c)
def fconst_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0c, []))
    
@to_bytecode(code=0x0d)
def fconst_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0d, []))
    
@to_bytecode(code=0x6e)
def fdiv(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6e, []))
    
@to_bytecode(code=0x22)
def fload_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x22, []))
    
@to_bytecode(code=0x23)
def fload_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x23, []))
    
@to_bytecode(code=0x24)
def fload_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x24, []))
    
@to_bytecode(code=0x25)
def fload_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x25, []))
    
@to_bytecode(code=0x6a)
def fmul(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6a, []))
    
@to_bytecode(code=0x76)
def fneg(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x76, []))
    
@to_bytecode(code=0x72)
def frem(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x72, []))
    
@to_bytecode(code=0xae)
def freturn(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xae, []))
    
@to_bytecode(code=0x43)
def fstore_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x43, []))
    
@to_bytecode(code=0x44)
def fstore_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x44, []))
    
@to_bytecode(code=0x45)
def fstore_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x45, []))
    
@to_bytecode(code=0x46)
def fstore_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x46, []))
    
@to_bytecode(code=0x66)
def fsub(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x66, []))
    
@to_bytecode(code=0x91)
def i2b(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x91, []))
    
@to_bytecode(code=0x92)
def i2c(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x92, []))
    
@to_bytecode(code=0x87)
def i2d(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x87, []))
    
@to_bytecode(code=0x86)
def i2f(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x86, []))
    
@to_bytecode(code=0x85)
def i2l(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x85, []))
    
@to_bytecode(code=0x93)
def i2s(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x93, []))
    
@to_bytecode(code=0x60)
def iadd(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x60, []))
    
@to_bytecode(code=0x2e)
def iaload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2e, []))
    
@to_bytecode(code=0x7e)
def iand(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7e, []))
    
@to_bytecode(code=0x4f)
def iastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4f, []))
    
@to_bytecode(code=0x2)
def iconst_m1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2, []))
    
@to_bytecode(code=0x3)
def iconst_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x3, []))
    
@to_bytecode(code=0x4)
def iconst_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x4, []))
    
@to_bytecode(code=0x5)
def iconst_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5, []))
    
@to_bytecode(code=0x6)
def iconst_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6, []))
    
@to_bytecode(code=0x7)
def iconst_4(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7, []))
    
@to_bytecode(code=0x8)
def iconst_5(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8, []))
    
@to_bytecode(code=0x6c)
def idiv(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6c, []))
    
@to_bytecode(code=0x1a)
def iload_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1a, []))
    
@to_bytecode(code=0x1b)
def iload_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1b, []))
    
@to_bytecode(code=0x1c)
def iload_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1c, []))
    
@to_bytecode(code=0x1d)
def iload_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1d, []))
    
@to_bytecode(code=0xfe)
def impdep1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xfe, []))
    
@to_bytecode(code=0xff)
def impdep2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xff, []))
    
@to_bytecode(code=0x68)
def imul(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x68, []))
    
@to_bytecode(code=0x74)
def ineg(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x74, []))
    
@to_bytecode(code=0x80)
def ior(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x80, []))
    
@to_bytecode(code=0x70)
def irem(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x70, []))
    
@to_bytecode(code=0xac)
def ireturn(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xac, []))
    
@to_bytecode(code=0x78)
def ishl(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x78, []))
    
@to_bytecode(code=0x7a)
def ishr(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7a, []))
    
@to_bytecode(code=0x3b)
def istore_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x3b, []))
    
@to_bytecode(code=0x3c)
def istore_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x3c, []))
    
@to_bytecode(code=0x3d)
def istore_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x3d, []))
    
@to_bytecode(code=0x3e)
def istore_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x3e, []))
    
@to_bytecode(code=0x64)
def isub(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x64, []))
    
@to_bytecode(code=0x7c)
def iushr(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7c, []))
    
@to_bytecode(code=0x82)
def ixor(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x82, []))
    
@to_bytecode(code=0x8a)
def l2d(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x8a, []))
    
@to_bytecode(code=0x89)
def l2f(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x89, []))
    
@to_bytecode(code=0x88)
def l2i(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x88, []))
    
@to_bytecode(code=0x61)
def ladd(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x61, []))
    
@to_bytecode(code=0x2f)
def laload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x2f, []))
    
@to_bytecode(code=0x7f)
def land(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7f, []))
    
@to_bytecode(code=0x50)
def lastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x50, []))
    
@to_bytecode(code=0x94)
def lcmp(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x94, []))
    
@to_bytecode(code=0x9)
def lconst_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x9, []))
    
@to_bytecode(code=0x0a)
def lconst_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0a, []))
    
@to_bytecode(code=0x6d)
def ldiv(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x6d, []))
    
@to_bytecode(code=0x1e)
def lload_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1e, []))
    
@to_bytecode(code=0x1f)
def lload_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x1f, []))
    
@to_bytecode(code=0x20)
def lload_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x20, []))
    
@to_bytecode(code=0x21)
def lload_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x21, []))
    
@to_bytecode(code=0x69)
def lmul(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x69, []))
    
@to_bytecode(code=0x75)
def lneg(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x75, []))
    
@to_bytecode(code=0x81)
def lor(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x81, []))
    
@to_bytecode(code=0x71)
def lrem(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x71, []))
    
@to_bytecode(code=0xad)
def lreturn(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xad, []))
    
@to_bytecode(code=0x79)
def lshl(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x79, []))
    
@to_bytecode(code=0x7b)
def lshr(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7b, []))
    
@to_bytecode(code=0x3f)
def lstore_0(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x3f, []))
    
@to_bytecode(code=0x40)
def lstore_1(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x40, []))
    
@to_bytecode(code=0x41)
def lstore_2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x41, []))
    
@to_bytecode(code=0x42)
def lstore_3(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x42, []))
    
@to_bytecode(code=0x65)
def lsub(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x65, []))
    
@to_bytecode(code=0x7d)
def lushr(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x7d, []))
    
@to_bytecode(code=0x83)
def lxor(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x83, []))
    
@to_bytecode(code=0xc2)
def monitorenter(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xc2, []))
    
@to_bytecode(code=0xc3)
def monitorexit(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xc3, []))
    
@to_bytecode(code=0x0)
def nop(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x0, []))
    
@to_bytecode(code=0x57)
def pop(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x57, []))
    
@to_bytecode(code=0x58)
def pop2(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x58, []))
    
@to_bytecode(code=0xb1)
def return_(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0xb1, []))
    
@to_bytecode(code=0x35)
def saload(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x35, []))
    
@to_bytecode(code=0x56)
def sastore(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x56, []))
    
@to_bytecode(code=0x5f)
def swap(loc, code):
    """
    :return (size, Bytecode)
    """
    return (1, Bytecode(loc, 0x5f, []))
    