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
        self.type_not_to_check = str()

    def is_digit(self, char: str):
        if char.isdigit():
            return True
        else:
            return False

    def is_dot(self, char: str):
        if char == '.':
            return True
        else:
            return False

    def is_alpha(self, char: str):
        if char.isalpha():
            return True
        else:
            return False

    def is_opening_bracket(self, char: str):
        if char == '(':
            return True
        else:
            return False

    def is_closing_bracket(self, char: str):
        if char == ')':
            return True
        else:
            return False

    def is_minus(self, char):
        if char == '-':
            return True
        else:
            return False

    def is_plus(self, char):
        if char == '+':
            return True
        else:
            return False

    def is_coma(self, char):
        if char == ',':
            return True
        else:
            return False

    def define_operand(self, char):
        if len(self.function) != 0:
            self.type_not_to_check = 'function'
            self.function += char
        else:
            self.type_not_to_check = 'operand'
            self.operand += char

    def define_operator(self, char):
        if len(self.operator) == 0:
            self.type_not_to_check = 'operator'
            if char == '-':
                self.operator += char
            elif char == '+':
                self.operator += char
            else:
                self.operator += char
        elif len(self.operator) != 0:
            self.type_not_to_check = 'operator'
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
        else:
            self.type_not_to_check = 'operator'
            self.operator += char

    def define_function(self, char):
        self.type_not_to_check = 'function'
        self.function += char

    '''
    Checks what attribute is filled currently except for resulting list and the one where current char in cycle will be
    merged.
    '''
    def check_which_types_filled(self, type_not_to_check):
        result = []
        for type in self.__dict__:
            if type not in ('resulting_list', 'type_not_to_check') and type != type_not_to_check and len(self.__dict__[type]) != 0:
                result.append(type)
        return result

    def add_token_to_resulting_dictionary(self, types):
        for type in types:
            value = self.__dict__[type]
            self.resulting_list.append({'type': type, 'value': value})
            self.__dict__[type] = ''

    def tokenize_expression(self, string: str):
        string = string.replace(',', ')(').lower()
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
                self.type_not_to_check = None
                self.opening_bracket += char
            elif self.is_closing_bracket(char):
                self.type_not_to_check = None
                self.closing_bracket += char
            elif char == ' ':
                self.type_not_to_check = None
            else:
                self.define_operator(char)
            attributes = self.check_which_types_filled(self.type_not_to_check)
            if len(attributes) != 0:
                self.add_token_to_resulting_dictionary(attributes)
        attributes = self.check_which_types_filled(type_not_to_check=None)
        self.add_token_to_resulting_dictionary(attributes)
        return self.resulting_list


