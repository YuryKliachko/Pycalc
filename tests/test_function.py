from unittest import TestCase
from pycalc.function import Function


class TestFunction(TestCase):
    def test_function_object(self):
        value = 'abs'
        index = 1
        function = abs
        test_function = Function(value, index, function)
        self.assertEqual(test_function.type, 'function')
        self.assertEqual(test_function.value, 'abs')
        self.assertEqual(test_function.index, 1)
        self.assertEqual(test_function.function, abs)