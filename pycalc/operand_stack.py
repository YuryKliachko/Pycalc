from pycalc.stack import Stack


class OperandStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def put_on_stack(self, item, stack_to_refresh):
        if stack_to_refresh.is_function_on_stack():
            item.type = 'attribute'
            self.container.append(item)
            stack_to_refresh.changed_last = False
            self.changed_last = True
        else:
            Stack.put_on_stack(self, item, stack_to_refresh)

    def remove_pre_last_item_from_stack(self):
        pre_last = self.container[self.length-2]
        del self.container[self.container.index(pre_last)]
        return pre_last

    def remove_args_from_stack(self, function_index):
        counter = -1
        for operand in self.container:
            counter += 1
            if operand.type == 'attribute' and operand.index > function_index:
                break
        arguments = tuple(operand.value for operand in self.container[counter:])
        self.container = self.container[:counter]
        return arguments
