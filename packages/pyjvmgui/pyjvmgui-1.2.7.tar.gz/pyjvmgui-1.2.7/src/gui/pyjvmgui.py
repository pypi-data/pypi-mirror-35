import os

from PySide2.QtCore import QSize, QUrl, Slot
from PySide2.QtQuick import QQuickView

from gui.abstractions.ops_to_bytecode import *
from gui.bytecodemodel import BytecodeModel
from gui.localsmodel import LocalsModel
from gui.opstackmodel import OperandStackModel

"""
These imports are required so that ops are initialized.
DO NOT REMOVE (there should be 5 + 5 + 4 = 14)
"""
from pyjvm.ops.ops_names import *
from pyjvm.ops.ops_arrays import *
from pyjvm.ops.ops_calc import *
from pyjvm.ops.ops_cond import *
from pyjvm.ops.ops_convert import *

from pyjvm.ops.ops_fields import *
from pyjvm.ops.ops_invokespecial import *
from pyjvm.ops.ops_invokestatic import *
from pyjvm.ops.ops_invokevirtual import *
from pyjvm.ops.ops_invokeinterface import *

from pyjvm.ops.ops_misc import *
from pyjvm.ops.ops_ret import *
from pyjvm.ops.ops_setget import *
from pyjvm.ops.ops_shift import *


class PyJvmGui(QQuickView):

    def __init__(self, executor, thread_idx, parent=None):
        super(PyJvmGui, self).__init__(parent)

        self.setResizeMode(QQuickView.SizeViewToRootObject)
        self.setMinimumSize(QSize(800, 600))
        self.setTitle("PyJVM - Thread " + str(thread_idx + 1))

        self.thread_idx = thread_idx
        self.executor = executor
        self.show_bytecode()

        self.rootContext().setContextProperty("app", self)

        qml_file_path_project = os.path.join(os.path.dirname(__file__), "qml", "App.qml")
        qml_file_path_home = os.path.join(os.path.expanduser("~"), ".pyjvmgui", "App.qml")

        if os.path.isfile(qml_file_path_project):
            qml_file_path = qml_file_path_project
        elif os.path.isfile(qml_file_path_home):
            qml_file_path = qml_file_path_home
        else:
            raise Exception("App.qml not found")

        self.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file_path)))

        self.show()

    def show_bytecode(self):
        # Bytecode
        bytecode = Bytecode.bytecode_list_from_code(self.executor.get_frame_for_thread(self.thread_idx).code)
        self.loc_to_idx = {}
        for i, code in enumerate(bytecode):
            self.loc_to_idx[code.loc] = i

        self.bytecode_model = BytecodeModel(bytecodes=bytecode)
        self.rootContext().setContextProperty("bytecode", self.bytecode_model)

        # Frame Information
        self.frame_info = self.executor.get_frame_for_thread(self.thread_idx).desc
        self.rootContext().setContextProperty("frameInfo", self.frame_info)

        # Operand Stack
        op_stack = self.executor.get_frame_for_thread(self.thread_idx).stack

        self.operand_stack_model = OperandStackModel(operands=op_stack)
        self.rootContext().setContextProperty("operandStack", self.operand_stack_model)

        # Locals & Args table
        locals = self.executor.get_frame_for_thread(self.thread_idx).args
        self.locals_model = LocalsModel(locals=locals)
        self.rootContext().setContextProperty("locals", self.locals_model)

    @Slot()
    def stepExecutor(self):
        frame_alive = self.executor.step_thread(self.thread_idx)
        self.show_bytecode()

    @Slot()
    def stepOut(self):
        self.executor.step_thread_until_frame_over(self.thread_idx)
        self.show_bytecode()

    @Slot(result=int)
    def getCurLoc(self):
        return self.loc_to_idx.get(self.executor.get_frame_for_thread(self.thread_idx).pc)
