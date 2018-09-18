from pycalc.operators_manager import OperatorsManager
from pycalc.functions_manager import FunctionsManager
from pycalc.error import Error
from pycalc.item import Item
from pycalc.operator_class import Operator
from pycalc.function import Function
from pycalc.bracket import Bracket


class Converter:
    def __init__(self):
        self.convertedList = []
        self.operatorManager = OperatorsManager()
        self.functionsManager = FunctionsManager()
        self.levelOfEnclosing = 0
        self.enclosingRequired = False
        self.itemIndex = -1
    
    def validateOperand(self, operand: str):
        if '.' in operand and operand.count('.') == 1:
            self.convertedList.append(Item(type='operand', value=float(operand), index=self.itemIndex))
        elif '.' not in operand:
            self.convertedList.append(Item(type='operand', value=int(operand), index=self.itemIndex))
        else:
            return Error(id=1, arg=operand)

    def validateOperator(self, operator: str):
        if self.operatorManager.isValidOperator(operator):
            if self.enclosingRequired:
                self.convertedList.append(Bracket(type='closingBracket', value=')', index=self.itemIndex))
                self.enclosingRequired = False
                self.itemIndex += 1
            elif len(self.convertedList) != 0:
                previous_item = self.convertedList[-1]
                if operator == '-' and previous_item.type == 'operator':
                    self.convertedList.append(Bracket(type='openingBracket', value='(', index=self.itemIndex))
                    self.enclosingRequired = True
                    self.itemIndex += 1
            priority = self.operatorManager.fetchOperatorsPriority(operator)
            operator_function = self.operatorManager.fetchOperatorsFunction(operator)
            self.convertedList.append(Operator(value=operator, index=self.itemIndex, function=operator_function, priority=priority))
        else:
            return Error(id=2, arg=operator)

    def validateFunction(self, function: str):
        if self.functionsManager.isValidFunction(function):
            function_object = self.functionsManager.fetchFunctionValue(function)
            if isinstance(function_object, float) or isinstance(function_object, int):
                self.convertedList.append(Item(type='operand', value=function_object, index=self.itemIndex))
            else:
                self.convertedList.append(Function(value=function, index=self.itemIndex, function=function_object))
        else:
            return Error(id=3, arg=function)

    def validateBracket(self, bracket):
        if bracket == '(':
            self.convertedList.append(Bracket(type='openingBracket', value=bracket, index=self.itemIndex))
            self.levelOfEnclosing += 1
        elif bracket == ')':
            if self.levelOfEnclosing > 0:
                self.levelOfEnclosing -= 1
                self.convertedList.append(Bracket(type='closingBracket', value=bracket, index=self.itemIndex))
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
            if self.enclosingRequired == True:
                self.convertedList.append(Bracket(type='closingBracket', value=')', index=self.itemIndex))
            return self.convertedList

