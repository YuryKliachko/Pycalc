from pycalc.item import Item


class Operator(Item):
    def __init__(self, value, index, function, priority):
        """Generates an instance of the Operator class inherited from the Item class, with additional attributes function
         and priority (to be received from operators manager)
        """
        super().__init__('operator', value, index)
        self.function = function
        self.priority = priority

