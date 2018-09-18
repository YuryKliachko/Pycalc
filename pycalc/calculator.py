from pycalc.tokenizer import Tokenizer
from pycalc.converter import Converter
from pycalc.error import Error
from pycalc.operators_manager import OperatorsManager
from pycalc.functions_manager import FunctionsManager
from pycalc.operator_stack import OperatorStack
from pycalc.operand_stack import OperandStack


class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.tokenizer = Tokenizer()
        self.converter = Converter()
        self.operatorsManager = OperatorsManager()
        self.functionsManager = FunctionsManager()
        self.prepared = []
        self.operandStack = OperandStack()
        self.operatorStack = OperatorStack()
        self.wasChangedLast = ''
        self.currentOperator = dict()


    def isReturnedAsError(self, item):
        if isinstance(item, Error):
            return True
        else:
            return False

    def getOperatorPriority(self, operator):
        priority = self.operatorsManager.fetchOperatorsPriority(operator)
        return priority

    def calculateOnStack(self):
        operatorOnstack = self.operatorStack.getLastItemFromStack()
        if operatorOnstack['type'] == 'function':
            operatorsFunction = self.functionsManager.fetchFunctionValue(operatorOnstack['name'])
            arguments = self.operandStack.remove_args_from_stack(operatorOnstack['index'])
            currentResult = operatorsFunction(*arguments)
        elif operatorOnstack['type'] == 'operator':
            operatorsFunction = self.operatorsManager.operatorsDict[operatorOnstack['value']]['function']
            firstOperand = self.operandStack.removePreLastItemFromStack()['value']
            secondOperand = self.operandStack.removeLastItemFromStack()['value']
            if firstOperand is None:
                if operatorOnstack['value'] in ['+', '-']:
                    firstOperand = 0
                else:
                    return Error(id=6, arg=operatorOnstack['value'])
            elif secondOperand is None:
                if operatorOnstack['type'] != 'function':
                    return Error(id=6, arg=operatorOnstack['value'])
            currentResult = operatorsFunction(firstOperand, secondOperand)
        else:
            currentResult = self.operandStack.getLastItemFromStack()['value']
            return currentResult
        if self.isReturnedAsError(currentResult) is False:
            self.operatorStack.removeLastItemFromStack()
            self.operandStack.putOnStack({'type': 'operand', 'value': currentResult, 'index': self.currentOperator['index']}, self.operatorStack)
        if self.operatorStack.isEmpty() is False:
            if self.getOperatorPriority(self.currentOperator['value']) >= self.getOperatorPriority(self.operatorStack.getLastItemFromStack()['value']):
                currentResult = self.calculateOnStack()
        return currentResult

    def prepareExpression(self):
        tokenized = self.tokenizer.tokenizeExpression(self.expression)
        converted = self.converter.convertToMath(tokenized)
        if isinstance(converted, Error):
            return converted
        self.prepared = converted

    def calculteResult(self):
        for item in self.prepared:
            if item['type'] == 'operand':
                self.operandStack.putOnStack(item, self.operatorStack)
            elif item['type'] == 'operator' or item['type'] == 'function':
                self.currentOperator = item
                if self.operatorStack.isEmpty():
                    self.operatorStack.putOnStack(item, self.operandStack)
                else:
                    current_operator_priority = self.getOperatorPriority(item['value'])
                    stack_operator_priority = self.getOperatorPriority(self.operatorStack.getLastItemFromStack()['value'])
                    if current_operator_priority < stack_operator_priority or self.currentOperator['value'] == '^' and self.operatorStack.getLastItemFromStack()['value'] == '^':
                        self.operatorStack.putOnStack(item, self.operandStack)
                    else:
                        currentResult = self.calculateOnStack()
                        if self.isReturnedAsError(currentResult):
                            return currentResult.raiseError()
                        self.operatorStack.putOnStack(self.currentOperator, self.operandStack)
            elif item['type'] == 'openingBracket':
                self.operatorStack.putOnStack(item, self.operandStack)
            else:
                for i in range(self.operatorStack.length):
                    currentResult = self.calculateOnStack()
                    if self.isReturnedAsError(currentResult):
                        return currentResult.raiseError()
                    if self.operatorStack.getLastItemFromStack()['type'] == 'openingBracket':
                        self.operatorStack.removeLastItemFromStack()
                        break
        if self.operatorStack.isEmpty():
            currentResult = self.operandStack.getLastItemFromStack()['value']
            return currentResult
        elif self.operatorStack.length == 1:
            currentResult = self.calculateOnStack()
            if self.isReturnedAsError(currentResult):
                return currentResult.raiseError()
        for i in range(self.operatorStack.length):
            currentResult = self.calculateOnStack()
            if self.operatorStack.length == 0:
                return currentResult
            if self.isReturnedAsError(currentResult):
                return currentResult.raiseError()
        return self.operandStack.getLastItemFromStack()['value']


cal = Calculator(expression='sin(-Pi/4)^1.5')
prepared = cal.prepareExpression()
if cal.isReturnedAsError(prepared):
    print(prepared.raiseError())
else:
    print(cal.calculteResult())
