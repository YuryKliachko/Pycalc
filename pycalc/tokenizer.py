class Tokenizer:
    def __init__(self):
        self.resultingList = list()
        self.operand = str()
        self.operator = str()
        self.function = str()
        self.openingBracket = ''
        self.closingBracket = ''

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
    '''
    Checks what attribute is filled currently except for resulting list and the one where current char in cycle will be
    merged.
    '''
    def checkIfAttributeFilled(self, attributeNotToCheck):
        for attribute in self.__dict__:
            if attribute != 'resultingList' and attribute != attributeNotToCheck and len(self.__dict__[attribute]) != 0:
                return attribute

    def addTokenToResultingDictinary(self, attribute):
        self.resultingList.append((attribute, self.__dict__[attribute]))

    def tokenizeExpression(self, expression: str):
        attributeNotToCheck = ''
        for char in expression.replace(' ', ''):
            if self.isDigit(char):
                attributeNotToCheck = 'operand'
                self.operand += char
            elif self.isDot(char):
                attributeNotToCheck = 'operand'
                self.operand += char
            elif self.isAlpha(char):
                attributeNotToCheck = 'function'
                self.function += char
            elif self.isOpenningBracket(char):
                attributeNotToCheck = 'openingBracket'
                self.openingBracket += char
            elif self.isClosingBracket(char):
                attributeNotToCheck = 'closingBracket'
                self.closingBracket += char
            attribute = self.checkIfAttributeFilled(attributeNotToCheck)
            if attribute is not None:
                self.addTokenToResultingDictinary(attribute=attribute)
                self.__dict__[attribute] = ''
        self.addTokenToResultingDictinary(attribute=attributeNotToCheck)
        return self.resultingList

d = Tokenizer()
print(d.tokenizeExpression('2*(2.56+3.14)sin(30)'))