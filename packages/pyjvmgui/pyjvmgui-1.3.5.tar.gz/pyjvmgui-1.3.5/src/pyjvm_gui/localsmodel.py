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


class LocalsModel(QAbstractListModel):
    IDX_ROLE = Qt.UserRole + 5
    VALUE_ROLE = Qt.UserRole + 6

    _roles = {IDX_ROLE: b"idx", VALUE_ROLE: b"value"}

    def __init__(self, locals, parent=None):
        super(LocalsModel, self).__init__()
        self.locals = locals
        self.currentIndex = 0

    def rowCount(self, *args, **kwargs):
        return len(self.locals)

    def data(self, q_modelindex, role=None):
        row = q_modelindex.row()

        if role == self.IDX_ROLE:
            return row

        if role == self.VALUE_ROLE:
            return str(self.locals[row])

    def roleNames(self):
        return self._roles
