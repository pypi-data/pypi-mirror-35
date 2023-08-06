import os

from PySide2.QtCore import QSize, QUrl, Slot
from PySide2.QtQuick import QQuickView

from gui.abstractions.ops_to_bytecode import *
from gui.bytecodemodel import BytecodeModel
from gui.localsmodel import LocalsModel
from gui.opstackmodel import OperandStackModel
from pyjvm.thread_state import ThreadState

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
    THREAD_GUIS = []

    def __init__(self, executor, thread_idx, parent=None):
        """

        :param executor: pyjvm.threadexecutor.ThreadExecutor
        :type executor: pyjvm.threadexecutor.ThreadExecutor
        :param thread_idx:
        :type thread_idx: int
        """
        super(PyJvmGui, self).__init__(parent)

        self.setResizeMode(QQuickView.SizeViewToRootObject)
        self.setMinimumSize(QSize(800, 600))

        self.setTitle("PyJVM - Thread {0} {1}".format(
            str(thread_idx + 1),
            "(daemon)" if executor.is_daemon() == 1 else ""
        ))

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
        frame = self.executor.get_frame_for_thread()
        if frame != None:
            bytecode = Bytecode.bytecode_list_from_code(frame.code)
            self.loc_to_idx = {}
            for i, code in enumerate(bytecode):
                self.loc_to_idx[code.loc] = i

        else:
            # Native method
            bytecode = []

        self.bytecode_model = BytecodeModel(bytecodes=bytecode)
        self.rootContext().setContextProperty("bytecode", self.bytecode_model)

        # Frame Information
        if frame != None:
            self.frame_info = frame.desc
            self.rootContext().setContextProperty("frameInfo", self.frame_info)
        else:
            self.rootContext().setContextProperty("frameInfo", "Native method")

        # Operand Stack
        if frame != None:
            op_stack = frame.stack
        else:
            op_stack = []

        self.operand_stack_model = OperandStackModel(operands=op_stack)
        self.rootContext().setContextProperty("operandStack", self.operand_stack_model)

        # Locals & Args table
        if frame != None:
            locals = frame.args
        else:
            locals = []

        self.locals_model = LocalsModel(locals=locals)
        self.rootContext().setContextProperty("locals", self.locals_model)

    @Slot()
    def stepExecutor(self):
        state = self.executor.step_thread()
        if state == ThreadState.DONE or (state == ThreadState.BLOCKED and len(self.executor.thread.vm.threads) == 1):
            self.close()
        self.show_bytecode()

    @Slot()
    def stepOut(self):
        state = self.executor.step_thread_until_frame_over()
        if state == ThreadState.DONE or (state == ThreadState.BLOCKED and len(self.executor.thread.vm.threads) == 1):
            self.close()
        self.show_bytecode()

    @Slot()
    def stepUntilDoneOrBlocked(self):
        state = self.executor.step_thread_until_done_or_blocked()
        if state == ThreadState.DONE or (state == ThreadState.BLOCKED and len(self.executor.thread.vm.threads) == 1):
            self.close()
        self.show_bytecode()

    @Slot(result=int)
    def getCurLoc(self):
        frame = self.executor.get_frame_for_thread()
        if frame != None:
            return self.loc_to_idx.get(self.executor.get_frame_for_thread().pc)
        else:
            return -1
