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

    '''
    Checks what attribute is filled currently except for resulting list and the one where current char in cycle will be
    merged.
    '''
    def checkWhichAttributesFilled(self, attributeNotToCheck):
        result = []
        for attribute in self.__dict__:
            if attribute != 'resultingList' and attribute != attributeNotToCheck and len(self.__dict__[attribute]) != 0:
                result.append(attribute)
        return result

    def addTokenToResultingDictinary(self, attributes):
        for attribute in attributes:
            if attribute is not None:
                type = attribute
                value = self.__dict__[attribute]
                self.resultingList.append({'type': type, 'value': value})
                self.__dict__[attribute] = ''

    def tokenizeExpression(self, string: str):
        string = string.replace(' ', '').lower()
        assert string != '', 'Expression cannot be empty!'
        attributeNotToCheck = ''
        for char in string:
            if self.isDigit(char):
                attributeNotToCheck = 'operand'
                self.operand += char
            elif self.isDot(char):
                attributeNotToCheck = 'operand'
                self.operand += char
            elif self.isComa(char):
                attributeNotToCheck = None
            elif self.isAlpha(char):
                attributeNotToCheck = 'function'
                self.function += char
            elif self.isOpenningBracket(char):
                attributeNotToCheck = None
                self.openingBracket = char
            elif self.isClosingBracket(char):
                attributeNotToCheck = None
                self.closingBracket = char
            elif self.isMinus(char):
                attributeNotToCheck = 'operator'
                if len(self.operator) == 0:
                    self.operator += char
                else:
                    if self.isMinus(self.operator[-1]):
                        self.operator = self.operator.replace(self.operator[-1], '+')
                    elif self.isPlus(self.operator[-1]):
                        self.operator = self.operator.replace(self.operator[-1], '-')
            elif self.isPlus(char):
                attributeNotToCheck = 'operator'
                if len(self.operator) == 0:
                    self.operator += char
            else:
                attributeNotToCheck = 'operator'
                self.operator += char
            attribute = self.checkWhichAttributesFilled(attributeNotToCheck)
            if attribute is not None:
                self.addTokenToResultingDictinary(attributes=attribute)
        self.addTokenToResultingDictinary(attributes=[attributeNotToCheck])
        return self.resultingList

