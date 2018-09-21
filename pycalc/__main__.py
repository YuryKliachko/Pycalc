from argparse import ArgumentParser, PARSER
from pycalc.calculator import Calculator


def main():
    parser = ArgumentParser()
    parser.add_argument('EXPRESSION', help='expression string to evaluate')
    args = parser.parse_args()
    calc = Calculator(expression=args.EXPRESSION)
    prepared = calc.prepare_expression()
    if calc.is_returned_as_error(prepared):
        print(prepared.raise_error())
    else:
        print(calc.calculate_result())


if __name__ == '__main__':
    main()
