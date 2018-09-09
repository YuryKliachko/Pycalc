from pycalc.calculator import Calculator

calc = Calculator()
operators = {
    '+': lambda x=0, y=0: x+y,
    '-': lambda x=0, y=0: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
    '%': lambda x, y: x%y,
    '//': lambda x, y: x//y,
    '^': lambda x, y: x**y,
    '==': lambda x, y: x==y,
    '>=': lambda x, y: x>=y
}

functions = {'sin': 1, 'cos': 2}

s = operators['^']

print(s(3, -2))