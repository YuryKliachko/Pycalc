from unittest import TestCase
from pycalc.bracket import Bracket


class TestBracket(TestCase):
    def test_bracket_object(self):
        type = 'test_bracket'
        value = '('
        index = 1
        test_bracket = Bracket(type, value, index)
        self.assertEqual(test_bracket.type, type)
        self.assertEqual(test_bracket.value, value)
        self.assertEqual(test_bracket.index, index)
