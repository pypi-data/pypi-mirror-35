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
