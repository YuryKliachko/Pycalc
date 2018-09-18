from pycalc.operand_stack import OperandStack
from pycalc.stack import Stack


class OperatorStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operatorStack'

    def putOnStack(self, item, stackToRefresh):
        if item['value'] in ('+', '-'):
            if self.changedLast is True or stackToRefresh.isEmpty() is True:
                stackToRefresh.putOnStack({'type': 'operand', 'value': 0, 'index': item['index']-1}, stackToRefresh=self)
        Stack.putOnStack(self, item, stackToRefresh)

    def isFunctionInStack(self):
        for operator in self.container:
            if operator['type'] == 'function':
                return True