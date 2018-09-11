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
        return self.operandStack[len(self.operandStack)-1]['value']

    def removeOperandFromStack(self):
        return self.operandStack.pop()

    def putOperatorOnStack(self, operator):
        self.operatorStack.append(operator)

    def getOperatorFromStack(self):
        return self.operatorStack[len(self.operatorStack)-1]['value']

    def removeOperatorFromStack(self):
        self.operatorStack.pop()

    def getOperatorPriority(self, operator):
        operatorOnStack = self.getOperatorFromStack()
        priority = self.operatorsManager.fetchOperatorsPriority(operatorOnStack)
        return priority

    def getNextItem(self, currentItemIndex):
        try:
            nextItem = self.prepared[currentItemIndex+1]['type']
            return nextItem
        except IndexError:
            return None

    def calculateOnStack(self):
        operator = self.getOperatorFromStack()
        operatorsFunction = self.operatorsManager.operatorsDict[operator]
        if operator in ('-', '+'):
            if self.previousItem == 'operand':
                firstOperand = self.removeOperandFromStack()
            elif self.previousItem == '' or self.previousItem != 'operand':
                firstOperand = 0
            if self.nextItem == 'operand':
                secondOperand = self.removeOperandFromStack()
            elif self.nextItem not in ('+', '-') or self.nextItem is None:
                return Error(id=6, arg=operator)
            else:
                secondOperand = 0
            return operatorsFunction(firstOperand, secondOperand)
        else:
            if self.previousItem == 'operand' and self.nextItem == 'operand':
                firstOperand = self.removeOperandFromStack()
                secondOperand = self.removeOperandFromStack()
                return operatorsFunction(firstOperand, secondOperand)
            else:
                return Error(id=6, arg=operator)


    def prepareExpression(self):
        tokenized = self.tokenizer.tokenizeExpression(self.expression)
        converted = self.converter.convertToMath(tokenized)
        if isinstance(converted, Error):
            return converted.raiseError()
        self.prepared = converted

    def calculteResult(self):
        for item in self.prepared:
            if item['type'] == 'operand':
                self.putOperandOnStack(item['value'])
            elif item['type'] == 'operator':
                if self.isOperatorStackEmpty():
                    self.putOperatorOnStack(item)
                else:
                    if self.getOperatorPriority(item['value']) > self.getOperatorPriority(self.getOperatorFromStack()):
                        self.putOperatorOnStack(item)
                    else:
                        currentResult = self.calculateOnStack()
                        self.putOperandOnStack(currentResult)
                        self.removeOperatorFromStack()
            elif item['type'] in ('openingBracket', 'closingbracket'):
                self.putOperatorOnStack(item['value'])

            self.previousItem = item['type']
            self.nextItem = self.getNextItem(currentItemIndex=self.prepared.index(item))
        if self.isOperatorStackEmpty():
            return self.getLastOperand()
        elif len(self.operatorStack) == 1:
            return self.calculateOnStack().raiseError()




cal = Calculator(expression='2+2')
cal.prepareExpression()
print(cal.calculteResult())