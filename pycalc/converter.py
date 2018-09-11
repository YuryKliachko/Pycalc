from pycalc.operators_manager import OperatorsManager
from pycalc.functions_manager import FunctionsManager
from pycalc.error import Error

class Converter:
    def __init__(self):
        self.convertedList = []
        self.operatorManager = OperatorsManager()
        self.functionsManager = FunctionsManager()
        self.levelOfEnclosing = 0
    
    def validateOperand(self, operand: str):
        if '.' in operand and operand.count('.') == 1 and not operand.startswith('.') and not operand.endswith('.'):
            self.convertedList.append({'type': 'operand', 'value': float(operand)})
        elif '.' not in operand:
            self.convertedList.append({'type': 'operand', 'value': int(operand)})
        else:
            return Error(id=1, arg=operand)

    def validateOperator(self, operator: str):
        if self.operatorManager.isValidOperator(operator):
            function = self.operatorManager.fetchOperatorsFunction(operator)
            priority = self.operatorManager.fetchOperatorsPriority(operator)
            self.convertedList.append({'type': 'operator', 'value': function, 'priority': priority})
        else:
            return Error(id=2, arg=operator)

    def validateFunction(self, function: str):
        if self.functionsManager.isValidFunction(function):
            value = self.functionsManager.fetchFunctionValue(function)
            self.convertedList.append({'type': 'function', 'value': value})
        else:
            return Error(id=3, arg=function)

    def validateBracket(self, bracket):
        if bracket == '(':
            self.convertedList.append({'type': 'openingBracket', 'level': self.levelOfEnclosing})
            self.levelOfEnclosing += 1
        elif bracket == ')':
            if self.levelOfEnclosing > 0:
                self.levelOfEnclosing -= 1
                self.convertedList.append({'type': 'closingBracket', 'level': self.levelOfEnclosing})
            else:
                return Error(id=4, arg='(')

    def convertToMath(self, tokenizedList):
        convertedList = []
        for item in tokenizedList:
            if item['type'] == 'operand':
                operand = self.validateOperand(item['value'])
                if isinstance(operand, Error):
                    return operand.raiseError()
            elif item['type'] is 'operator':
                operator = self.validateOperator(item['value'])
                if isinstance(operator, Error):
                    return operator.raiseError()
            elif item['type'] == 'function':
                function = self.validateFunction(item['value'])
                if isinstance(function, Error):
                    return function.raiseError()
            elif item['type'] == 'openingBracket' or item['type'] == 'closingBracket':
                bracket = self.validateBracket(item['value'])
                if isinstance(bracket, Error):
                    return bracket.raiseError()
            else:
                convertedList.append(item)
        if self.levelOfEnclosing > 0:
            return Error(id=5, arg=')').raiseError()
        else:
            return self.convertedList

'''
conv = Converter()
for i in conv.convertToMath([{'type': 'operator', 'value': '-'},
                          {'type': 'function', 'value': 'pow'},
                          {'type': 'openingBracket', 'value': '('},
                          {'type': 'openingBracket', 'value': '('},
                          {'type': 'operand', 'value': '3.4'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'closingBracket', 'value': ')'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operand', 'value': '5'},
                          {'type': 'closingBracket', 'value': ')'}]):
'''


