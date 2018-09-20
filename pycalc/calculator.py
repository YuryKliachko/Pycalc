from pycalc.tokenizer import Tokenizer
from pycalc.converter import Converter
from pycalc.error import Error
from pycalc.operators_manager import OperatorsManager
from pycalc.functions_manager import FunctionsManager
from pycalc.operator_stack import OperatorStack
from pycalc.operand_stack import OperandStack
from pycalc.item import Item


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
        self.currentOperator = dict()

    def is_returned_as_error(self, item):
        if isinstance(item, Error):
            return True
        else:
            return False

    def calculateOnStack(self):
        operatorOnstack = self.operatorStack.lastItem
        if operatorOnstack.type == 'function':
            operatorsFunction = operatorOnstack.function
            arguments = self.operandStack.remove_args_from_stack(operatorOnstack.index)
            currentResult = operatorsFunction(*arguments)
        elif operatorOnstack.type == 'operator':
            operatorsFunction = operatorOnstack.function
            firstOperand = self.operandStack.removePreLastItemFromStack()
            secondOperand = self.operandStack.removeLastItemFromStack()
            if firstOperand is None:
                if operatorOnstack.value in ['+', '-']:
                    firstOperand = Item(type='operand', value=0, index=self.currentOperator.index)
                else:
                    return Error(id=6, arg=operatorOnstack.value)
            elif secondOperand is None:
                if operatorOnstack.type != 'function':
                    return Error(id=6, arg=operatorOnstack.value)
            currentResult = operatorsFunction(firstOperand.value, secondOperand.value)
        else:
            currentResult = self.operandStack.lastItem.value
            return currentResult
        if self.is_returned_as_error(currentResult):
            return currentResult
        else:
            self.operatorStack.removeLastItemFromStack()
            self.operandStack.putOnStack(Item(type='operand', value=currentResult, index=self.currentOperator.index), self.operatorStack)
            if self.operatorStack.isEmpty() is False:
                if self.currentOperator.priority >= self.operatorStack.lastItem.priority:
                    currentResult = self.calculateOnStack()
        return currentResult

    def prepareExpression(self):
        tokenized = self.tokenizer.tokenize_expression(self.expression)
        converted = self.converter.convert_to_math(tokenized)
        if isinstance(converted, Error):
            return converted
        self.prepared = converted

    def calculteResult(self):
        for item in self.prepared:
            if item.type == 'operand':
                self.operandStack.putOnStack(item, self.operatorStack)
            elif item.type == 'operator' or item.type == 'function':
                self.currentOperator = item
                if self.operatorStack.isEmpty():
                    self.operatorStack.putOnStack(item, self.operandStack)
                else:
                    if self.currentOperator.priority < self.operatorStack.lastItem.priority or self.currentOperator.value == '^' and self.operatorStack.lastItem.value == '^':
                        self.operatorStack.putOnStack(item, self.operandStack)
                    else:
                        currentResult = self.calculateOnStack()
                        if self.is_returned_as_error(currentResult):
                            return currentResult.raiseError()
                        self.operatorStack.putOnStack(self.currentOperator, self.operandStack)
            elif item.type == 'opening_bracket':
                self.operatorStack.putOnStack(item, self.operandStack)
            else:
                for i in range(self.operatorStack.length):
                    currentResult = self.calculateOnStack()
                    if self.is_returned_as_error(currentResult):
                        return currentResult.raiseError()
                    if self.operatorStack.lastItem.type == 'opening_bracket':
                        self.operatorStack.removeLastItemFromStack()
                        break
        if self.operatorStack.isEmpty():
            currentResult = self.operandStack.lastItem.value
            return currentResult
        elif self.operatorStack.length == 1:
            currentResult = self.calculateOnStack()
            if self.is_returned_as_error(currentResult):
                return currentResult.raiseError()
        for i in range(self.operatorStack.length):
            currentResult = self.calculateOnStack()
            if self.operatorStack.length == 0:
                return currentResult
            if self.is_returned_as_error(currentResult):
                return currentResult.raiseError()
        return self.operandStack.lastItem.value


cal = Calculator(expression='2(2+2)')
prepared = cal.prepareExpression()
if cal.is_returned_as_error(prepared):
    print(prepared.raiseError())
else:
    print(cal.calculteResult())

