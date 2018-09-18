from unittest import TestCase
from pycalc.tokenizer import Tokenizer


class TestTokenizer(TestCase):

    def test_plus(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenizeExpression('2+2')
        self.assertEqual([{'type': 'operand', 'value': '2'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operand', 'value': '2'}], result)

    def test_double_plus(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenizeExpression('2++2')
        self.assertEqual([{'type': 'operand', 'value': '2'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operand', 'value': '2'}], result)

    def test_minus(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenizeExpression('5-2')
        self.assertEqual([{'type': 'operand', 'value': '5'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operand', 'value': '2'}], result)

    def test_math_operator_1(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenizeExpression('1^3')
        self.assertEqual([{'type': 'operand', 'value': '1'},
                          {'type': 'operator', 'value': '^'},
                          {'type': 'operand', 'value': '3'}], result)

    def test_math_module(self):
        tokenizer = Tokenizer()
        result = tokenizer.tokenizeExpression('1//3')
        self.assertEqual([{'type': 'operand', 'value': '1'},
                          {'type': 'operator', 'value': '//'},
                          {'type': 'operand', 'value': '3'}], result)