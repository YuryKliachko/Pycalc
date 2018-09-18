from pycalc.item import Item


class Function(Item):
    def __init__(self, value, index, function):
        Item.__init__(self, 'function', value, index)
        self.function = function
        self.priority = 0
