from unittest import TestCase
from pycalc.operators_manager import OperatorsManager


class TestOperatorsManager(TestCase):
    def setUp(self):
        self.operators_manager = OperatorsManager()

    def test_is_valid_operator_positive(self):
        test_operator = '//'
        result = self.operators_manager.is_valid_operator(test_operator)
        self.assertEqual(result, True)

    def test_is_valid_operator_nagtive(self):
        test_operator = '**'
        result = self.operators_manager.is_valid_operator(test_operator)
        self.assertEqual(result, False)

    def test_fetch_operators_function(self):
        test_opeartor = '//'
        result = self.operators_manager.fetch_operators_function(test_opeartor)
        self.assertEqual(callable(result), True)

    def test_fetch_operators_priority(self):
        test_operator = '//'
        result = self.operators_manager.fetch_operators_priority(test_operator)
        self.assertIsInstance(result, int)