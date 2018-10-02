from pycalc.error import Error

class Tokenizer:
    def __init__(self):
        self.resulting_list = list()
        self.operand = str()
        self.operator = str()
        self.function = str()
        self.coma = str()
        self.opening_bracket = str()
        self.closing_bracket = str()
        self.item_not_to_check = str()
        self.coma = str()

    def is_digit(self, char: str):
        """Checks if char is digit"""
        if char.isdigit():
            return True
        else:
            return False

    def is_dot(self, char: str):
        """Checks if char is dot"""
        if char == '.':
            return True
        else:
            return False

    def is_alpha(self, char: str):
        """Checks if char is alphabetic"""
        if char.isalpha():
            return True
        else:
            return False

    def is_opening_bracket(self, char: str):
        """Checks is char is an opening bracket"""
        if char == '(':
            return True
        else:
            return False

    def is_closing_bracket(self, char: str):
        """Checks if char is a closing bracket"""
        if char == ')':
            return True
        else:
            return False

    def is_minus(self, char):
        """Checks id char is a minus"""
        if char == '-':
            return True
        else:
            return False

    def is_plus(self, char):
        """Checks if char is a plus"""
        if char == '+':
            return True
        else:
            return False

    def is_coma(self, char):
        """Checks if char is a coma"""
        if char == ',':
            return True
        else:
            return False

    def define_operand(self, char):
        """Defines where to add a char. If previous chars added to a function, current one will also be added
         to the function. Otherwise, a char will be added to an operand."""
        if len(self.function) != 0:
            self.item_not_to_check = 'function'
            self.function += char
        else:
            self.item_not_to_check = 'operand'
            self.operand += char

    def define_operator(self, char):
        """Defines if char should be added to the operator as it is or not. Firstly, method checks whether
        operator is already filled or not. If yes, then the char is added to the operator as it is.
        If the operator is not empty, there are a few conditions.
        If char is minus and the operator is plus, the operator will be changed to minus.
        If char is minus and the operator has minus value, then the operator will be changed to a plus.
        If a char is minus and the operator neither plus nor minus, then throw current operator value to
        resulting list and assign minus to the operator.
        If char is plus, not to add it to the operator. And finally, if char naither plus nor minus, it will be added to
        the operator.
        """
        if len(self.operator) == 0:
            self.item_not_to_check = 'operator'
            self.operator += char
        else:
            self.item_not_to_check = 'operator'
            if char == '-':
                if self.operator == '+':
                    self.operator = '-'
                elif self.operator == '-':
                    self.operator = '+'
                else:
                    self.add_token_to_resulting_dictionary(['operator'])
                    self.operator += char
            elif char == '+':
                return
            else:
                self.operator += char

    def define_function(self, char):
        self.item_not_to_check = 'function'
        self.function += char

    def check_which_items_filled(self, item_not_to_check):
        """
        Checks what item is filled currently except for resulting list and the one where current char in cycle will be
        merged. If method receives item_not_to_check as None, all items except for resulting list will be checked.
        returns result as a list of item names.
        """
        result = []
        for item in self.__dict__:
            if item not in ('resulting_list', 'item_not_to_check') and item != item_not_to_check and len(self.__dict__[item]) != 0:
                result.append(item)
        return result

    def add_token_to_resulting_dictionary(self, items):
        """Adds a dictionary with token and value to the resulting list and refreshes an added item"""
        for item in items:
            value = self.__dict__[item]
            self.resulting_list.append({'type': item, 'value': value})
            self.__dict__[item] = ''

    def tokenize_expression(self, string: str):
        """For each char in a string, method checks a value for a char and calls corrsponding "define" method.
        In the end, it uses check_which_items_filled method to get list of items to be added to the resulting list, adds
        them and returns resulting list.
        In case a string is empty, method raises an exception."""
        string = string.lower()
        if string == '':
            return Error(id=9)
        for char in string:
            if self.is_digit(char):
                self.define_operand(char)
            elif self.is_dot(char):
                self.define_operand(char)
            elif self.is_alpha(char):
                self.define_function(char)
            elif self.is_opening_bracket(char):
                self.item_not_to_check = None
                self.opening_bracket += char
            elif self.is_closing_bracket(char):
                self.item_not_to_check = None
                self.closing_bracket += char
            elif char == ' ':
                self.item_not_to_check = None
            elif self.is_coma(char):
                self.item_not_to_check = None
                self.coma += char
            else:
                self.define_operator(char)
            attributes = self.check_which_items_filled(self.item_not_to_check)
            if len(attributes) != 0:
                self.add_token_to_resulting_dictionary(attributes)
        attributes = self.check_which_items_filled(item_not_to_check=None)
        self.add_token_to_resulting_dictionary(attributes)
        return self.resulting_list


