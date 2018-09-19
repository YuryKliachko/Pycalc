from unittest import TestCase
from pycalc.tokenizer import Tokenizer


class TestTokenizer(TestCase):

    def test_plus(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('2+2')
        self.assertEqual([{'type': 'operand', 'value': '2'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operand', 'value': '2'}], result)

    def test_double_plus(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('2++2')
        self.assertEqual([{'type': 'operand', 'value': '2'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operand', 'value': '2'}], result)

    def test_minus(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('5-2')
        self.assertEqual([{'type': 'operand', 'value': '5'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operand', 'value': '2'}], result)

    def test_math_operator(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('1^3')
        self.assertEqual([{'type': 'operand', 'value': '1'},
                          {'type': 'operator', 'value': '^'},
                          {'type': 'operand', 'value': '3'}], result)

    def test_math_module(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('1//3')
        self.assertEqual([{'type': 'operand', 'value': '1'},
                          {'type': 'operator', 'value': '//'},
                          {'type': 'operand', 'value': '3'}], result)


    def test_math_function(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('sin(30)')
        self.assertEqual([{'type': 'function', 'value': 'sin'},
                          {'type': 'opening_bracket', 'value': '('},
                          {'type': 'operand', 'value': '30'},
                          {'type': 'closing_bracket', 'value': ')'}], result)

    def test_math_function_with_two_args(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('log10(30, 45)')
        self.assertEqual([{'type': 'function', 'value': 'log10'},
                          {'type': 'opening_bracket', 'value': '('},
                          {'type': 'operand', 'value': '30'},
                          {'type': 'closing_bracket', 'value': ')'},
                          {'type': 'opening_bracket', 'value': '('},
                          {'type': 'operand', 'value': '45'},
                          {'type': 'closing_bracket', 'value': ')'}], result)

    def test_fractional_operand(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenize_expression('2+2.104')
        self.assertEqual([{'type': 'operand', 'value': '2'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operand', 'value': '2.104'}], result)