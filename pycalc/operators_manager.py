from pycalc.error import Error


class OperatorsManager:
    def __init__(self):
        """
        Generates an instance of the OperatorsManager class, the operators dictionary attribute contains a name of an
        operator as a key and dictionary with lambda function and priority as a value
        """
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
        """
        Returns True if an operator is in operators dictionary, otherwise returns False
        """
        if operator in self.operators_dict.keys():
            return True
        else:
            return False

    def fetch_operators_function(self, operator):
        """
        Retrieves and returns an operator function from the operators dictionary
        """
        operators_function = self.operators_dict[operator]['function']
        return operators_function

    def fetch_operators_priority(self, operator):
        """
        Retrieves and returns an operator priority from the operators dictionary
        """
        priority = self.operators_dict[operator]['priority']
        return priority

