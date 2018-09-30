from unittest import TestCase
from pycalc.functions_manager import FunctionsManager


class TestFunctionsManager(TestCase):

    def setUp(self):
        self.function_manager = FunctionsManager()

    def test_is_valid_function_positive(self):
        func = 'sin'
        result= self.function_manager.is_valid_function(func)
        self.assertEqual(result, True)

    def test_is_valid_function_negative(self):
        func = 'sos'
        result= self.function_manager.is_valid_function(func)
        self.assertEqual(result, False)

    def test_fetch_function_value(self):
        func = 'round'
        result = self.function_manager.fetch_function_value(func)
        self.assertEqual(result, round)

    def test_add_new_dict(self):
        new_module = __import__('time')
        new_dict = new_module.__dict__
        self.function_manager.add_new_dict(new_dict)
        for func in new_dict:
            self.assertIn(func, self.function_manager.functions_dict)