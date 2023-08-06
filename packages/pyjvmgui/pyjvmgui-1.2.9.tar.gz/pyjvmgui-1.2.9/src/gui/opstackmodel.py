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
