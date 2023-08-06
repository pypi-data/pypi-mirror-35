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

from PySide2.QtCore import QAbstractListModel, Qt


class BytecodeModel(QAbstractListModel):
    LOC_ROLE = Qt.UserRole + 1
    OP_ROLE = Qt.UserRole + 2
    OPERAND_ROLE = Qt.UserRole + 3

    _roles = {LOC_ROLE: b"loc", OP_ROLE: b"op", OPERAND_ROLE: b"operands"}

    def __init__(self, bytecodes, parent=None):
        super(BytecodeModel, self).__init__()
        self.bytecodes = bytecodes
        self.currentIndex = 0

    def rowCount(self, *args, **kwargs):
        return len(self.bytecodes)

    def data(self, q_modelindex, role=None):
        row = q_modelindex.row()

        if role == self.LOC_ROLE:
            return str(self.bytecodes[row].loc)

        if role == self.OP_ROLE:
            return str(self.bytecodes[row].name)

        if role == self.OPERAND_ROLE:
            return str(self.bytecodes[row].operands)

    def roleNames(self):
        return self._roles
