from pycalc.tokenizer import Tokenizer
from pycalc.converter import Converter
from pycalc.error import Error
from pycalc.operators_manager import OperatorsManager


class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.tokenizer = Tokenizer()
        self.converter = Converter()
        self.operatorsManager = OperatorsManager()
        self.prepared = []
        self.operandStack = []
        self.operatorStack = []
        self.wasChangedLast = ''
        self.currentOperator = dict()

    def isOperandStackEmpty(self):
        if len(self.operandStack) == 0:
            return True
        else:
            return False

    def isOperatorStackEmpty(self):
        if len(self.operatorStack) == 0:
            return True
        else:
            return False

    def putOperandOnStack(self, operand):
        self.operandStack.append(operand)
        self.wasChangedLast = 'operandStack'

    def getLastOperand(self):
        return self.operandStack[len(self.operandStack)-1]

    def removeLastOperandFromStack(self):
        length = len(self.operandStack)
        if length > 0:
            return self.operandStack.pop()
        else:
            return None

    def removePreLastOperandFromStack(self):
        length = len(self.operandStack)
        preLast = self.operandStack[length - 2]
        del self.operandStack[self.operandStack.index(preLast)]
        return preLast

    def putOperatorOnStack(self, operator):
        if operator['value'] in ('+', '-'):
            if self.wasChangedLast == 'operatorStack' or self.isOperandStackEmpty():
                self.putOperandOnStack(0)
        self.operatorStack.append(operator)
        self.wasChangedLast = 'operatorStack'

    def getOperatorFromStack(self):
        return self.operatorStack[len(self.operatorStack)-1]

    def removeOperatorFromStack(self):
        self.operatorStack.pop()

    def getOperatorPriority(self, operator):
        priority = self.operatorsManager.fetchOperatorsPriority(operator)
        return priority

    def isReturnedAsError(self, item):
        if isinstance(item, Error):
            return True
        else:
            return False

    def calculateOnStack(self):
        operatorOnstack = self.getOperatorFromStack()
        operatorsFunction = self.operatorsManager.operatorsDict[operatorOnstack['value']]['function']
        if operatorOnstack['value'] == '(':
            return self.getLastOperand()
        else:
            firstOperand = self.removePreLastOperandFromStack()
            secondOperand = self.removeLastOperandFromStack()
            if firstOperand is None:
                if operatorOnstack['value'] in ['+', '-']:
                    firstOperand = 0
                else:
                    return Error(id=6, arg=operatorOnstack['value'])
            elif secondOperand is None:
                    return Error(id=6, arg=operatorOnstack['value'])
        currentResult = operatorsFunction(firstOperand, secondOperand)
        if self.isReturnedAsError(currentResult) is False:
            self.putOperandOnStack(currentResult)
            self.removeOperatorFromStack()
        if self.isOperatorStackEmpty() is False:
            if self.getOperatorPriority(self.currentOperator['value']) >= self.getOperatorPriority(self.getOperatorFromStack()['value']):
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
                self.putOperandOnStack(item['value'])
            elif item['type'] == 'operator':
                self.currentOperator = item
                if self.isOperatorStackEmpty():
                    self.putOperatorOnStack(item)
                else:
                    if self.getOperatorPriority(item['value']) < self.getOperatorPriority(self.getOperatorFromStack()['value']):
                        self.putOperatorOnStack(item)
                    else:
                        currentResult = self.calculateOnStack()
                        if self.isReturnedAsError(currentResult):
                            return currentResult.raiseError()
                        self.putOperatorOnStack(self.currentOperator)
            elif item['type'] == 'openingBracket':
                self.putOperatorOnStack(item)
            else:
                for i in range(len(self.operatorStack)):
                    currentResult = self.calculateOnStack()
                    if self.isReturnedAsError(currentResult):
                        return currentResult.raiseError()
                    if self.getOperatorFromStack()['type'] == 'openingBracket':
                        self.removeOperatorFromStack()
                        break
        if self.isOperatorStackEmpty():
            return self.getLastOperand()
        elif len(self.operatorStack) == 1:
            currentResult = self.calculateOnStack()
            if self.isReturnedAsError(currentResult):
                return currentResult.raiseError()
        for i in range(len(self.operatorStack)):
            currentResult = self.calculateOnStack()
            if self.isReturnedAsError(currentResult):
                return currentResult.raiseError()
        return self.getLastOperand()


cal = Calculator(expression='2.0^(2.0^2.0*2.0^2.0)')
prepared = cal.prepareExpression()
if cal.isReturnedAsError(prepared):
    print(prepared.raiseError())
else:
    print(cal.calculteResult())
