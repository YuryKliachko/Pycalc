import math

class FunctionsManager:
    def __init__(self):
        self.functionsDict = {'pow': pow, 'abs': abs, 'round': round}
        self.functionsDict.update(math.__dict__)

    def isValidFunction(self, function):
        if function in self.functionsDict.keys():
            return True
        else:
            return False

    def fetchFunctionValue(self, function):
        value = self.functionsDict[function]
        return value

    def addNewDict(self, dictionary: dict):
        self.functionsDict.update(dictionary)