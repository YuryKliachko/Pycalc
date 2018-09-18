from pycalc.item import Item


class Operator(Item):
    def __init__(self, value, index, function, priority):
        Item.__init__(self, 'operator', value, index)
        self.function = function
        self.priority = priority

