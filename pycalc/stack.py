class Stack:
    def __init__(self):
        """
        Generates an instance of the Stack object.
        """
        self.container = list()  # All items will be added to the container when put_on_stack method invoked
        self.changed_last = False  # This attribute changes to True when item is being put on the stack

    @property
    def length(self):
        """
        Returns the container length
        """
        return len(self.container)

    def is_empty(self):
        """
        Returns True if no items on a stack, otherwise returns False
        """
        if self.length == 0:
            return True
        else:
            return False

    def put_on_stack(self, item, stack_to_refresh):
        """
        Appends an item to the container and refreshes the changed_last flag of a stack that wasn't changed by
        assigning False value
        """
        self.container.append(item)
        stack_to_refresh.changed_last = False
        self.changed_last = True

    @property
    def last_item(self):
        """Returns a last item from stack"""
        return self.container[self.length-1] if self.length != 0 else None

    def remove_last_item_from_stack(self):
        """Remove and returns a last item from stack"""
        if self.length > 0:
            return self.container.pop()
        else:
            return None


