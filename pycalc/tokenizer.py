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
                self.resultingList.append((type, value))
                self.__dict__[attribute] = ''

    def tokenizeExpression(self, string: str):
        assert string != '', 'Expression cannot be empty!'
        attributeNotToCheck = ''
        for char in string.replace(' ', '').lower():
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
                attributeNotToCheck = None
                self.openingBracket = char
            elif self.isClosingBracket(char):
                attributeNotToCheck = None
                self.closingBracket = char
            else:
                attributeNotToCheck = 'operator'
                self.operator += char
            attribute = self.checkIfAttributeFilled(attributeNotToCheck)
            if attribute is not None:
                self.addTokenToResultingDictinary(attributes=attribute)
        self.addTokenToResultingDictinary(attributes=[attributeNotToCheck])
        return self.resultingList

d = Tokenizer()
print(d.tokenizeExpression('2 (Pi!= .1244.43244'))

