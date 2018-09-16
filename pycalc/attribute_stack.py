from pycalc.stack import Stack


class AttributeStack(Stack):
    def __init__(self):
        Stack.__init__(self)

    def putOnStack(self, item, stackToRefresh):
        item['type'] = 'attribute'
        self.container.append(item)
        stackToRefresh.changedLast = False
        self.changedLast = True

    def removeArgmentsFromStack(self, fictionIndex):
        counter = -1
        for argument in self.container:
            counter += 1
            if argument['index'] > fictionIndex:
                break
            return self.container[counter:]