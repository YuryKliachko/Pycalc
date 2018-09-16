class Tokenizer:
    def __init__(self):
        self.resultingList = list()
        self.operand = str()
        self.operator = str()
        self.function = str()
        self.coma = str()
        self.openingBracket = ''
        self.closingBracket = ''
        self.attributeNotToCheck = str()
    def isDigit(self, char: str):
        if char.isdigit():
            return True
        else:
            return False

    def isDot(self, char: str):
        if char == '.':
            return True
        else:
            return False

    def isAlpha(self, char: str):
        if char.isalpha():
            return True
        else:
            return False

    def isOpenningBracket(self, char: str):
        if char == '(':
            return True
        else:
            return False

    def isClosingBracket(self, char: str):
        if char == ')':
            return True
        else:
            return False

    def isMinus(self, char):
        if char == '-':
            return True
        else:
            return False

    def isPlus(self, char):
        if char == '+':
            return True
        else:
            return False

    def isComa(self, char):
        if char == ',':
            return True
        else:
            return False

    def defineOperand(self, char):
        if len(self.function) != 0:
            self.attributeNotToCheck = 'function'
            self.function += char
        else:
            self.attributeNotToCheck = 'operand'
            self.operand += char


    def defineOperator(self, char):
        if len(self.operator) == 0:
            self.attributeNotToCheck = 'operator'
            if char == '-':
                self.operator += char
            elif char == '+':
                self.operator += char
            else:
                self.operator += char
        elif len(self.operator) != 0:
            self.attributeNotToCheck = 'operator'
            if char == '-':
                if self.operator == '+':
                    self.operator = '-'
                elif self.operator == '-':
                    self.operator = '+'
                else:
                    self.addTokenToResultingDictinary(['operator'])
                    self.operator += char
            elif char == '+':
                return
            else:
                self.operator += char
        else:
            self.attributeNotToCheck = 'operator'
            self.operator += char

    def defineFunction(self, char):
        self.attributeNotToCheck = 'function'
        self.function += char

    '''
    Checks what attribute is filled currently except for resulting list and the one where current char in cycle will be
    merged.
    '''
    def checkWhichAttributesFilled(self, attributeNotToCheck):
        result = []
        for attribute in self.__dict__:
            if attribute not in ('resultingList', 'attributeNotToCheck') and attribute != attributeNotToCheck and len(self.__dict__[attribute]) != 0:
                result.append(attribute)
        return result

    def addTokenToResultingDictinary(self, attributes):
        for attribute in attributes:
            value = self.__dict__[attribute]
            self.resultingList.append({'type': attribute, 'value': value})
            self.__dict__[attribute] = ''

    def tokenizeExpression(self, string: str):
        string = string.replace(' ', '').replace(',', ')(').lower()
        assert string != '', 'Expression cannot be empty!'
        for index, char in enumerate(string):
            if self.isDigit(char):
                self.defineOperand(char)
            elif self.isDot(char):
                self.defineOperand(char)
            elif self.isAlpha(char):
                self.defineFunction(char)
            elif self.isOpenningBracket(char):
                self.attributeNotToCheck = None
                self.openingBracket += char
            elif self.isClosingBracket(char):
                self.attributeNotToCheck = None
                self.closingBracket += char
            else:
                self.defineOperator(char)
            attributes = self.checkWhichAttributesFilled(self.attributeNotToCheck)
            if len(attributes) != 0:
                self.addTokenToResultingDictinary(attributes)
        attributes = self.checkWhichAttributesFilled(attributeNotToCheck=None)
        self.addTokenToResultingDictinary(attributes)
        return self.resultingList



#t = Tokenizer()
#print(t.tokenizeExpression('1+(2+3*2'))