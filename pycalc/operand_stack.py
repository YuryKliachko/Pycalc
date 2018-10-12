from pycalc.stack import Stack


class OperandStack(Stack):
    def put_on_stack(self, item, stack_to_refresh):
        """
        Method overrides the same method in the superclass with additional checking if an operators stack contains
        functions and changes item type to 'argument'
        """
        if stack_to_refresh.is_function_on_stack():
            item.type = 'argument'
            self.container.append(item)
            stack_to_refresh.changed_last = False
            self.changed_last = True
        else:
            super().put_on_stack(item, stack_to_refresh)

    def remove_pre_last_item_from_stack(self):
        """
        Removes and returns a pre-last item from stack
        """
        pre_last = self.container[self.length-2]
        del self.container[self.container.index(pre_last)]
        return pre_last

    def remove_arguments_from_stack(self, function_index):
        """
        Searches for all items, which have 'argument' type, remove them from stack and returns as a tuple
        """
        counter = -1
        for operand in self.container:
            counter += 1
            if operand.type == 'argument' and operand.index > function_index:
                break
        arguments = tuple(operand.value for operand in self.container[counter:])
        self.container = self.container[:counter]
        return arguments
