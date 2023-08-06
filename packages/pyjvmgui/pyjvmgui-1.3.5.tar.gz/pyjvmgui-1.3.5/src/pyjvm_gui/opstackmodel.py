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


class OperandStackModel(QAbstractListModel):
    OPERAND_ROLE = Qt.UserRole + 4

    _roles = {OPERAND_ROLE: b"operands"}

    def __init__(self, operands, parent=None):
        super(OperandStackModel, self).__init__()
        self.operands = operands

    def rowCount(self, *args, **kwargs):
        return len(self.operands)

    def data(self, q_modelindex, role=None):
        row = q_modelindex.row()

        if role == self.OPERAND_ROLE:
            return str(self.operands[row])

    def roleNames(self):
        return self._roles
