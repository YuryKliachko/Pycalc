from pycalc.stack import Stack

class OperandStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operandStack'

    def removePreLastItemFromStack(self):
        preLast = self.container[self.length-2]
        del self.container[self.container.index(preLast)]
        return preLast['value']

