from pycalc.operators_manager import OperatorsManager
from pycalc.functions_manager import FunctionsManager
from pycalc.error import Error

class Converter:
    def __init__(self):
        self.convertedList = []
        self.operatorManager = OperatorsManager()
        self.functionsManager = FunctionsManager()
        self.levelOfEnclosing = 0
        self.itemIndex = -1
    
    def validateOperand(self, operand: str):
        if '.' in operand and operand.count('.') == 1:
            self.convertedList.append({'type': 'operand', 'value': float(operand), 'index': self.itemIndex})
        elif '.' not in operand:
            self.convertedList.append({'type': 'operand', 'value': int(operand), 'index': self.itemIndex})
        else:
            return Error(id=1, arg=operand)

    def validateOperator(self, operator: str):
        if self.operatorManager.isValidOperator(operator):
            priority = self.operatorManager.fetchOperatorsPriority(operator)
            self.convertedList.append({'type': 'operator', 'value': operator, 'priority': priority, 'index': self.itemIndex})
        else:
            return Error(id=2, arg=operator)

    def validateFunction(self, function: str):
        if self.functionsManager.isValidFunction(function):
            value = self.functionsManager.fetchFunctionValue(function)
            self.convertedList.append({'type': 'function', 'value': value, 'index': self.itemIndex})
        else:
            return Error(id=3, arg=function)

    def validateBracket(self, bracket):
        if bracket == '(':
            self.convertedList.append({'type': 'openingBracket', 'value': '(', 'index': self.itemIndex})
            self.levelOfEnclosing += 1
        elif bracket == ')':
            if self.levelOfEnclosing > 0:
                self.levelOfEnclosing -= 1
                self.convertedList.append({'type': 'closingBracket', 'value': ')', 'index': self.itemIndex})
            else:
                return Error(id=4, arg='(')

    def convertToMath(self, tokenizedList):
        convertedList = []
        for item in tokenizedList:
            self.itemIndex += 1
            if item['type'] == 'operand':
                operand = self.validateOperand(item['value'])
                if isinstance(operand, Error):
                    return operand
            elif item['type'] is 'operator':
                operator = self.validateOperator(item['value'])
                if isinstance(operator, Error):
                    return operator
            elif item['type'] == 'function':
                function = self.validateFunction(item['value'])
                if isinstance(function, Error):
                    return function
            elif item['type'] == 'openingBracket' or item['type'] == 'closingBracket':
                bracket = self.validateBracket(item['value'])
                if isinstance(bracket, Error):
                    return bracket
            else:
                convertedList.append(item)
        if self.levelOfEnclosing > 0:
            return Error(id=5, arg=')')
        else:
            return self.convertedList

'''
#conv = Converter()
#for i in conv.convertToMath([{'type': 'operator', 'value': '-'},
                          {'type': 'function', 'value': 'pow'},
                          {'type': 'openingBracket', 'value': '('},
                          {'type': 'openingBracket', 'value': '('},
                          {'type': 'operand', 'value': '.34'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'closingBracket', 'value': ')'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operand', 'value': '5.'},
                          {'type': 'closingBracket', 'value': ')'}]):

print(i)
'''