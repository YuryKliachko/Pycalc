from pycalc.stack import Stack
from pycalc.item import Item


class OperatorStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.name = 'operatorStack'

    def put_on_stack(self, item, stack_to_refresh):
        if item.value in ('+', '-'):
            if self.changed_last is True or stack_to_refresh.is_empty() is True:
                stack_to_refresh.put_on_stack(Item(type='operand', value=0, index=item.index-1), stack_to_refresh=self)
        Stack.put_on_stack(self, item, stack_to_refresh)

    def is_function_on_stack(self):
        for operator in self.container:
            if operator.type == 'function':
                return True