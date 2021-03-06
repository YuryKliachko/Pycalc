from pycalc.item import Item


class Bracket(Item):
    """
    Bracket class inherited from the Item class with additional parameter priority, which always has a constant value
    """
    def __init__(self, type, value, index):
        super().__init__(type, value, index)
        self.priority = 10
