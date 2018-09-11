class Calculator:
    def __init__(self, expression: list):
        self.expression = expression

    def calculteResult(self, expression):
        pass



cal = Calculator(expression=[('operand', 3),
                             ['openingBracket', '('],
                             ('function', 'cos'),
                             ('operator', '*', 3),
                             ('operand', 1244.43244),
                             ('operator', '+', 4),
                             ['openingBracket', '('],
                             ('operand', 2),
                             ('operator', '+', 4),
                             ('operand', 3),
                             ['closingBracket', ')'],
                             ['closingBracket', ')']])

#print(cal.calculteResult(expression=cal.expression))