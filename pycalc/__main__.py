from argparse import ArgumentParser
from pycalc.calculator import Calculator
from pycalc.error import Error
from pycalc.functions_manager import FunctionsManager

parser = ArgumentParser(description='Pure-python command-line calculator.', prog='pycalc')
parser.add_argument('-m', '--use-modules', help='additional modules to use', metavar='MODULE [MODULE ...]')
parser.add_argument('EXPRESSION', help='expression string to evaluate')
args = parser.parse_args()


def main():
    """This function gather positional arguments entered invokes calculation. Wrapped in try block to catch error
    messages while preparing expression and calculating itself
    """
    if args.use_modules:
        for module in args.use_modules.split(' '):
            user_module = __import__(module)
            FunctionsManager.add_new_dict(user_module.__dict__)
    try:
        calc = Calculator(expression=args.EXPRESSION)
        calc.prepare_expression()
        print(calc.calculate_result())
    except Error as error:
        print(error.text)


if __name__ == '__main__':
    main()
