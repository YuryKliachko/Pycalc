from argparse import ArgumentParser, PARSER
from pycalc.calculator import Calculator
from pycalc.error import Error


def main():
    parser = ArgumentParser()
    parser.add_argument('EXPRESSION', help='expression string to evaluate')
    args = parser.parse_args()
    try:
        calc = Calculator(expression=args.EXPRESSION)
        calc.prepare_expression()
        print(calc.calculate_result())
    except Error as error:
        print(error.text)


if __name__ == '__main__':
    main()
