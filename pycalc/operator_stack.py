from pycalc.stack import Stack
from pycalc.item import Item


class OperatorStack(Stack):
    def __init__(self):
        """Fully inherits __init__ method from the Stack class with no changes"""
        super().__init__()

    def put_on_stack(self, item, stack_to_refresh):
        """
        Overrides the same method in the superclass and additionally puts an item with zero value on a operand stack
        if an operator is plus or minus and there is no operand before the operator.
        """
        if item.value in ('+', '-'):
            if self.changed_last is True or stack_to_refresh.is_empty() is True:
                stack_to_refresh.put_on_stack(Item(type='operand', value=0, index=item.index-1), stack_to_refresh=self)
        super().put_on_stack(item, stack_to_refresh)

    def is_function_on_stack(self):
        """Returns True if at least one function is on stack"""
        for operator in self.container:
            if operator.type == 'function':
                return True
