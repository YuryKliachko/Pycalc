from pycalc.error import Error

class OperatorsManager:
    def __init__(self):
        self.operatorsDict = {
            'function': {'priority': 0},
            '(': {'function': None, 'priority': 10},
            ')': {'function': None, 'priority': 10},
            '+': {'function': lambda x=0, y=0: x + y, 'priority': 4},
            '-': {'function': lambda x=0, y=0: x - y, 'priority': 4},
            '*': {'function': lambda x, y: x * y, 'priority': 3},
            '/': {'function': lambda x, y: Error(id=8, arg='/') if y == 0 else x/y, 'priority': 3},
            '%': {'function': lambda x, y: x % y, 'priority': 3},
            '//': {'function': lambda x, y: x // y, 'priority': 3},
            '^': {'function': lambda x, y: Error(id=7, arg='^') if x < 0 and isinstance(y, float) else x ** y, 'priority': 1},
            '==': {'function': lambda x, y: x == y, 'priority': 9},
            '!=': {'function': lambda x, y: x != y, 'priority': 9},
            '>': {'function': lambda x, y: x > y, 'priority': 9},
            '<': {'function': lambda x, y: x < y, 'priority': 9},
            '>=': {'function': lambda x, y: x >= y, 'priority': 9},
            '<=': {'function': lambda x, y: x <= y, 'priority': 9},
        }

    def isValidOperator(self, operator):
        if operator in self.operatorsDict.keys():
            return True
        else:
            return False

    def fetchOperatorsFunction(self, operator):
        operatorsFunction = self.operatorsDict[operator]['function']
        return operatorsFunction

    def fetchOperatorsPriority(self, operator):
        priority = self.operatorsDict[operator]['priority']
        return priority

