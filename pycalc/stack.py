class Stack:
    def __init__(self):
        self.container = list()
        self.changedLast = False

    @property
    def length(self):
        return len(self.container)

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def putOnStack(self, item, stackToRefresh):
        self.container.append(item)
        stackToRefresh.changedLast = False
        self.changedLast = True

    def getLastItemFromSrack(self):
        return self.container[self.length-1]

    def removeLastItemFromStack(self):
        if self.length > 0:
            return self.container.pop()
        else:
            return None

