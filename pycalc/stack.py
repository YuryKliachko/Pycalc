class Stack:
    def __init__(self):
        self.container = list()
        self.changed_last = False

    @property
    def length(self):
        return len(self.container)

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def put_on_stack(self, item, stack_to_refresh):
        self.container.append(item)
        stack_to_refresh.changed_last = False
        self.changed_last = True

    @property
    def last_item(self):
        return self.container[self.length-1]

    def remove_last_item_from_stack(self):
        if self.length > 0:
            return self.container.pop()
        else:
            return None


