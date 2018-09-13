from pycalc.stack import Stack

class OperandStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operandStack'


