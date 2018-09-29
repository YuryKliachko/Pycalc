from unittest import TestCase
from pycalc.error import Error


class TestError(TestCase):
    def test_error(self):
        id = 3
        arg = 'sos'
        try:
            Error(id, arg)
        except Error as error:
            self.assertEqual(error.text, 'ERROR: Unsupported function sos!')
