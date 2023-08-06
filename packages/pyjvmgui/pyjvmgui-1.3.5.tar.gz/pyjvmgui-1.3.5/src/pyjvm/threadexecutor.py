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

from pyjvm.thread_state import ThreadState


class ThreadExecutor:

    def __init__(self, thread):
        """

        :type thread: pyjvm.thread.Thread
        :param thread: The Thread
        """

        self.thread = thread

    def get_frame_for_thread(self):
        """
        :return: Current frame of the specified thread
        :rtype: pyjvm.frame.Frame
        """
        if len(self.thread.frame_stack) > 0:
            return self.thread.frame_stack[-1]
        else:
            return None

    def is_daemon(self):
        vm = self.thread.vm
        java_thread = vm.heap[self.thread.java_thread[1]]
        return java_thread.fields["daemon"] == 1

    # def run_all(self):
    #     """
    #     Executes all threads
    #     :return: None
    #     """
    #     while True:
    #         if not self.step_all_threads(quota=1000):
    #             break

    def step_thread(self, quota=1):
        """
        Run a single bytecode from thread with index thread_idx
        :param quota: Number of bytecodes to execute
        :type quota: int
        :return: the ThreadState
        """
        return self.thread.vm.run_thread_my(self.thread, quota=quota)

    def step_thread_until_frame_over(self):
        """
        Keep executing until this frame is popped.
        :return: void
        """
        frame_stack_depth = len(self.thread.frame_stack)

        if frame_stack_depth <= 1:
            from pyjvmgui import logger
            logger.warn("Trying to step out from frame depth " + str(frame_stack_depth))
            return

        next_stack_depth = frame_stack_depth

        while frame_stack_depth <= next_stack_depth:
            state = self.step_thread()
            next_stack_depth = len(self.thread.frame_stack)

            if state == ThreadState.BLOCKED:
                return state

            elif state == ThreadState.RUNNING and frame_stack_depth > next_stack_depth:
                return state

            elif state == ThreadState.RUNNING and frame_stack_depth <= next_stack_depth:
                continue

            elif state == ThreadState.DONE:
                return state

            else:
                raise Exception("Unknown frame state")

    def step_thread_until_done_or_blocked(self):
        return self.thread.vm.run_thread_my(self.thread, quota=-1)

    # def step_all_threads(self, quota=1):
    #     """
    #     Run quota bytecodes for every thread
    #     :param quota: n of bytecodes (default 1)
    #     :return: true if any thread is still alive after exec, false otherwise
    #     """
    #     any_alive = False
    #     for thread_idx in range(len(self.thread.vm.threads)):
    #         thread = self.thread.vm.threads[thread_idx]
    #         if thread.is_alive:
    #             self.step_thread(thread_idx, quota)
    #             if len(thread.frame_stack) == 0:
    #                 self.kill_thread(thread)
    #             else:
    #                 any_alive = True
    #     return any_alive and self.thread.vm.non_daemons > 0

    # def kill_thread(self, thread):
    #     """
    #     Kill the specified thread
    #     :param thread: the thread
    #     :return: None
    #     """
    #
    #     print "killing thread"
    #     thread.is_alive = False
    #     j_thread = self.thread.vm.heap[thread.java_thread[1]]
    #     assert j_thread is not None
    #     for o in j_thread.waiting_list:
    #         o.is_notified = True
    #     java_thread = self.thread.vm.heap[thread.java_thread[1]]
    #     if java_thread.fields["daemon"] == 0:
    #         self.thread.vm.non_daemons -= 1
    #         if self.thread.vm.non_daemons == 0:
    #             pass
