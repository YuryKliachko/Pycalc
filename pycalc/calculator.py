
class Calculator:
    def __init__(self, expression: list):
        self.expression = expression

    def calculteResult(self, expression):
        maxLevel = 0
        for each in expression:
            if each[0] == 'openingBracket':
                each.append(maxLevel)
                maxLevel += 1
            elif each[0] == 'closingBracket':
                if maxLevel > 0:
                    maxLevel -= 1
                    each.append(maxLevel)
                else:
                    return 'Opening bracket required!'
        if maxLevel > 0:
            return 'Closing bracket required!'
        return expression



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