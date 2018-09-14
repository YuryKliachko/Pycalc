from pycalc.stack import Stack

class OperandStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operandStack'

    def removePreLastItemFromStack(self):
        if self.length == 1:
            if self.changedLast == False:
                preLast = self.container[0]
                del self.container[0]
            else:
                return None
        elif self.length == 0:
            return None
        else:
            preLast = self.container[self.length-2]
            del self.container[self.length-2]
        return preLast


