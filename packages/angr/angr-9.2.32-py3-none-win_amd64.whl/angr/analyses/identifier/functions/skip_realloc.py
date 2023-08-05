import logging

from ..func import Func, TestData
from ....errors import SimMemoryError


l = logging.getLogger(name=__name__)

class realloc(Func):
    def __init__(self):
        super().__init__() #pylint disable=useless-super-delegation

    def num_args(self):
        return 2

    def args(self): #pylint disable=no-self-use
        return ["ptr", "size"]

    def get_name(self):
        return "realloc"

    def gen_input_output_pair(self):
        return None

    def pre_test(self, func, runner):
        # we should not get a nonzero output from the function with a value this large
        num = 0xffff0000
        test_input = [0, num]
        test_output = [None, None]
        return_val = None
        max_steps = 10
        test = TestData(test_input, test_output, return_val, max_steps)
        state = runner.get_out_state(func, test)
        if state is not None and state.solver.eval(state.regs.eax) != 0:
            return False

        # we should be able to get different outputs if we call malloc multiple times
        num = 0x80
        test_input = [0, num]
        test_output = [None, None]
        return_val = None

        max_steps = 10
        test = TestData(test_input, test_output, return_val, max_steps)
        returned_locs = []
        state = runner.get_out_state(func, test)
        if state is None:
            return False
        returned_locs.append(state.solver.eval(state.regs.eax))

        for i in range(10): #pylint disable=unused-variable
            state = runner.get_out_state(func, test, initial_state=state)
            if state is None:
                return False
            returned_locs.append(state.solver.eval(state.regs.eax))

        # if we got the same value 2x it didnt work
        if len(set(returned_locs)) != len(returned_locs):
            return False

        # if we got 0 it didn't work
        if any(a == 0 for a in returned_locs):
            return False

        # if they are all multiples of 0x1000 it seems to be always calling allocate
        if all(a % 0x1000 == returned_locs[0] % 0x1000 for a in returned_locs):
            return False

        # they all should be writable/readable
        try:
            if any(state.solver.eval(state.memory.permissions(a)) & 3 != 3 for a in returned_locs):
                return False
        except SimMemoryError:
            return False

        # we should get different values if we try with a different size
        num = 0x320
        test_input = [0, num]
        test_output = [None, None]
        return_val = None
        max_steps = 10
        test = TestData(test_input, test_output, return_val, max_steps)
        returned_locs2 = []
        state = runner.get_out_state(func, test)
        if state is None:
            return False
        returned_locs2.append(state.solver.eval(state.regs.eax))

        for i in range(10):
            state = runner.get_out_state(func, test, initial_state=state)
            if state is None:
                return False
            returned_locs2.append(state.solver.eval(state.regs.eax))

        if returned_locs == returned_locs2:
            return False

        return True
