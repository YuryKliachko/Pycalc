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

    def checkIfAttributeFilled(self):
        for attribute in self.__dict__:
            if attribute != 'resultingList' and len(self.__dict__[attribute]) != 0:
                return attribute

    def addTokenToResultingDictinary(self, attribute):
        self.resultingList.append((attribute, self.__dict__[attribute]))

    def tokenizeExpression(self, expression: str):
        for char in expression.replace(' ', ''):
            if self.isDigit(char):
                attribute = self.checkIfAttributeFilled()
                if attribute is not None:
                    self.addTokenToResultingDictinary(attribute=attribute)
                    self.__dict__[attribute] = ''
                self.operand += char
            elif self.isDot(char):
                attribute = self.checkIfAttributeFilled()
                if attribute is not None:
                    self.addTokenToResultingDictinary(attribute=attribute)
                    self.__dict__[attribute] = ''
                self.operand += char
            elif self.isAlpha(char):
                attribute = self.checkIfAttributeFilled()
                if attribute is not None:
                    self.addTokenToResultingDictinary(attribute=attribute)
                    self.__dict__[attribute] = ''
                self.function += char
            elif self.isOpenningBracket(char):
                attribute = self.checkIfAttributeFilled()
                if attribute is not None:
                    self.addTokenToResultingDictinary(attribute=attribute)
                    self.__dict__[attribute] = ''
                self.openingBracket += char
            elif self.isClosingBracket(char):
                attribute = self.checkIfAttributeFilled()
                if attribute is not None:
                    self.addTokenToResultingDictinary(attribute=attribute)
                    self.__dict__[attribute] = ''
                self.closingBracket += char
        return self.resultingList

d = Tokenizer()
print(d.tokenizeExpression('2*(2.56+3.14)'))