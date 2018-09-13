from pycalc.tokenizer import Tokenizer
from pycalc.converter import Converter
from pycalc.error import Error
from pycalc.operators_manager import OperatorsManager


class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.itemCounter = 0
        self.tokenizer = Tokenizer()
        self.converter = Converter()
        self.operatorsManager = OperatorsManager()
        self.prepared = []
        self.operandStack = []
        self.operatorStack = []
        self.previousItem = str()
        self.nextItem = str()

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

    def getLastOperand(self):
        return self.operandStack[len(self.operandStack)-1]

    def removeLastOperandFromStack(self):
        return self.operandStack.pop()

    def removePreLastOperandFromStack(self):
        preLast = self.operandStack[len(self.operandStack)-2]
        del self.operandStack[self.operandStack.index(preLast)]
        return preLast

    def putOperatorOnStack(self, operator):
        self.operatorStack.append(operator)

    def getOperatorFromStack(self):
        return self.operatorStack[len(self.operatorStack)-1]['value']

    def removeOperatorFromStack(self):
        self.operatorStack.pop()

    def getOperatorPriority(self, operator):
        priority = self.operatorsManager.fetchOperatorsPriority(operator)
        return priority

    def getNextItem(self, currentItemIndex):
        try:
            nextItem = self.prepared[currentItemIndex+1]
            return nextItem
        except IndexError:
            return None

    def isReturnedAsError(self, item):
        if isinstance(item, Error):
            return True
        else:
            return False

    def calculateOnStack(self):
        operator = self.getOperatorFromStack()
        operatorsFunction = self.operatorsManager.operatorsDict[operator]['function']
        if operator in ('-', '+'):
            if self.previousItem == 'operand':
                firstOperand = self.removePreLastOperandFromStack()
            elif self.previousItem == '' or self.previousItem != 'operand':
                firstOperand = 0
            if self.nextItem['type'] == 'operand':
                secondOperand = self.removeLastOperandFromStack()
            elif self.nextItem['value'] not in ('+', '-') or self.nextItem is None:
                currentResult = Error(id=6, arg=operator)
            else:
                secondOperand = 0
            currentResult = operatorsFunction(firstOperand, secondOperand)
        else:
            if self.previousItem == 'operand' and self.nextItem == 'operand':
                firstOperand = self.removePreLastOperandFromStack()
                secondOperand = self.removeLastOperandFromStack()
                currentResult = operatorsFunction(firstOperand, secondOperand)
            else:
                currentResult = Error(id=6, arg=operator)
        if self.isReturnedAsError(currentResult) is False:
            self.putOperandOnStack(currentResult)
            self.removeOperatorFromStack()
        return currentResult

    def prepareExpression(self):
        tokenized = self.tokenizer.tokenizeExpression(self.expression)
        converted = self.converter.convertToMath(tokenized)
        if isinstance(converted, Error):
            return converted.raiseError()
        self.prepared = converted

    def calculteResult(self):
        for item in self.prepared:
            self.itemCounter += 1
            if item['type'] == 'operand':
                self.putOperandOnStack(item['value'])
            elif item['type'] == 'operator':
                currentIndex = self.prepared.index(item, self.itemCounter-1, len(self.expression))
                self.nextItem = self.getNextItem(currentItemIndex=currentIndex)
                if self.isOperatorStackEmpty():
                    self.putOperatorOnStack(item)
                else:
                    if self.getOperatorPriority(item['value']) < self.getOperatorPriority(self.getOperatorFromStack()):
                        self.putOperatorOnStack(item)
                    else:
                        currentResult = self.calculateOnStack()
                        if self.isReturnedAsError(currentResult):
                            return currentResult.raiseError()
                        self.putOperatorOnStack(item)
            elif item['type'] in ('openingBracket'):
                self.putOperatorOnStack(item)
            else:
                for i in range(len(self.operatorStack)):
                    currentResult = self.calculateOnStack()
                    if self.isReturnedAsError(currentResult):
                        return currentResult.raiseError()
                    if self.getOperatorFromStack() == '(':
                        self.removeOperatorFromStack()
                        break
            if item['type'] != 'closingBracket':
                self.previousItem = item['type']
        if self.isOperatorStackEmpty():
            return self.getLastOperand()
        elif len(self.operatorStack) == 1:
            return self.calculateOnStack()
        for i in range(len(self.operatorStack)):
            currentResult = self.calculateOnStack()
            if self.isReturnedAsError(currentResult):
                return currentResult.raiseError()
        return self.getLastOperand()




cal = Calculator(expression='2--2')
prepared = cal.prepareExpression()
if cal.isReturnedAsError(prepared):
    print(prepared.raiseError())
print(cal.calculteResult())