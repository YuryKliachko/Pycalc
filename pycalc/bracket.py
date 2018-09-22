from pycalc.item import Item


class Bracket(Item):
    def __init__(self, type, value, index):
        Item.__init__(self, type, value, index)
        self.priority = 10
