from argparse import ArgumentParser, PARSER
from pycalc.calculator import Calculator


def main():
    parser = ArgumentParser()
    parser.add_argument('EXPRESSION', help='expression string to evaluate')
    args = parser.parse_args()
    calc = Calculator(expression=args.EXPRESSION)
    prepared = calc.prepareExpression()
    if calc.is_returned_as_error(prepared):
        print(prepared.raiseError())
    else:
        print(calc.calculteResult())


if __name__ == '__main__':
    main()
