from pycalc.operand_stack import OperandStack
from pycalc.stack import Stack

class OperatorStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operatorStack'
