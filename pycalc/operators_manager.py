from pycalc.error import Error


class OperatorsManager:
    def __init__(self):
        self.operators_dict = {
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

    def is_valid_operator(self, operator):
        if operator in self.operators_dict.keys():
            return True
        else:
            return False

    def fetch_operators_function(self, operator):
        operators_function = self.operators_dict[operator]['function']
        return operators_function

    def fetch_operators_priority(self, operator):
        priority = self.operators_dict[operator]['priority']
        return priority

