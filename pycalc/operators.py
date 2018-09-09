from pycalc.calculator import Calculator
import math

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

functions = {'pow': pow, 'cos': 2}

s = functions['pow'](2, 2)
print(s)