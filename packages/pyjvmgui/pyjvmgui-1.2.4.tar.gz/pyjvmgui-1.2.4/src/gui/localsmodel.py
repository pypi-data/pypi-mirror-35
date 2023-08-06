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
