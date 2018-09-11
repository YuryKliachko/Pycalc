from pycalc.tokenizer import Tokenizer
from pycalc.converter import Converter
from pycalc.error import Error


class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.tokenizer = Tokenizer()
        self.converter = Converter()

    def calculteResult(self):
        tokenized = self.tokenizer.tokenizeExpression(self.expression)
        converted = self.converter.convertToMath(tokenized)
        print(converted)



cal = Calculator(expression='sin(2, 3)')

print(cal.calculteResult())