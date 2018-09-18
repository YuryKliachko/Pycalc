from pycalc.stack import Stack

class OperandStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operandStack'

    def putOnStack(self, item, stackToRefresh):
        if stackToRefresh.isFunctionInStack():
            item.type = 'attribute'
            self.container.append(item)
            stackToRefresh.changedLast = False
            self.changedLast = True
        else:
            Stack.putOnStack(self, item, stackToRefresh)

    def removePreLastItemFromStack(self):
        preLast = self.container[self.length-2]
        del self.container[self.container.index(preLast)]
        return preLast

    def remove_args_from_stack(self, function_index):
        counter = -1
        for operand in self.container:
            counter += 1
            if operand.type == 'attribute' and operand.index > function_index:
                break
        arguments = tuple(operand.value for operand in self.container[counter:])
        self.container = self.container[:counter]
        return arguments
