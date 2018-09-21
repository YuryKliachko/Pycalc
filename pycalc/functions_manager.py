import math


class FunctionsManager:
    def __init__(self):
        self.functions_dict = {'pow': pow, 'abs': abs, 'round': round}
        self.functions_dict.update(math.__dict__)

    def isValidFunction(self, function):
        if function in self.functions_dict.keys():
            return True
        else:
            return False

    def fetchFunctionValue(self, function):
        value = self.functions_dict[function]
        return value

    def addNewDict(self, dictionary: dict):
        self.functions_dict.update(dictionary)