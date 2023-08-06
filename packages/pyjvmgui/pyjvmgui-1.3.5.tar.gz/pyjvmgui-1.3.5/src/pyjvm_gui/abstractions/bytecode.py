# PyJVM GUI
# Copyright (C) 2018 Matevz Fabjancic (mf6422@student.uni-lj.si)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from pyjvm import bytecode as bytecodeutil


class Bytecode:

    def __init__(self, loc, opcode, operands):
        """

        :param opcode: numeric representation of this bytecode instruction
        :param operands: array of operands
        """
        self.loc = loc
        self.opcode = opcode
        self.name = bytecodeutil.get_operation_name(hex(opcode))
        self.operands = operands

    def __str__(self):
        return "{0}\t{1} {2}".format(self.loc, self.name, str(self.operands))

    @staticmethod
    def bytecode_list_from_code(code):
        """
        Construct a list of Bytecode instances
        :param code: bytes representing a frame's bytecode
        :return: array of Bytecode instances
        """
        bytecodes = []
        cur_loc = 0
        while cur_loc < len(code):
            opcode = hex(ord(code[cur_loc]))
            disasm_oper = bytecodeutil.get_to_bytecode(opcode)
            size, bytecode = disasm_oper(cur_loc, code)
            cur_loc += size
            bytecodes.append(bytecode)
        return bytecodes
