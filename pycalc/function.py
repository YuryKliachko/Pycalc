from pycalc.item import Item


class Function(Item):
    def __init__(self, value, index, function):
        """Generates an instance of a Function class inherited from Item class, with additional attributes function
        (intended lambda function received from functions manager) and priority which has
         a constant value (highest one)"""
        super().__init__('function', value, index)
        self.function = function
        self.priority = 0
