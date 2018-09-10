import math

operators = {
    '+': {'function': lambda x=0, y=0: x+y, 'priority': 4},
    '-': {'function': lambda x=0, y=0: x-y, 'priority': 4},
    '*': {'function': lambda x, y: x*y, 'priority': 3},
    '/': {'function': lambda x, y: x/y if y != 0 else "Devision by zero!", 'priority': 3},
    '%': {'function': lambda x, y: x%y, 'priority': 3},
    '//': {'function': lambda x, y: x//y, 'priority': 3},
    '^': {'function': lambda x, y: x**y, 'priority': 1},
    '==': {'function': lambda x, y: x==y, 'priority': 9},
    '!=': {'function': lambda x, y: x!=y, 'priority': 9},
    '>': {'function': lambda x, y: x>y, 'priority': 9},
    '<': {'function': lambda x, y: x<y, 'priority': 9},
    '>=': {'function': lambda x, y: x>=y, 'priority': 9},
    '<=': {'function': lambda x, y: x<=y, 'priority': 9},
}

functions = {'pow': pow, 'abs': abs, 'round': round}
functions.update(math.__dict__)


