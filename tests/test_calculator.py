from unittest import TestCase
from pycalc.calculator import Calculator

class TestCalculator(TestCase):

    def test_unary_1(self):
        calc = Calculator(expression='-13')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(-13, result)

    def test_unary_2(self):
        calc = Calculator(expression='6-(-13)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(19, result)

    def test_unary_3(self):
        calc = Calculator(expression='1---1')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(0, result)

    def test_unary_4(self):
        calc = Calculator(expression='-+---+-1')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(-1, result)

    def test_operation_priority_1(self):
        calc = Calculator(expression='1+2*2')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(5, result)

    def test_operation_priority_2(self):
        calc = Calculator(expression='1+(2+3*2)*3')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(25, result)

    def test_operation_priority_3(self):
        calc = Calculator(expression='10*(2+1)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(30, result)

    def test_operation_priority_4(self):
        calc = Calculator(expression='10^(2+1)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(1000, result)

    def test_operation_priority_5(self):
        calc = Calculator(expression='100/3^2')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(11.11111111111111, result)

    def test_operation_priority_6(self):
        calc = Calculator(expression='100/3%2')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(1.3333333333333357, result)

    def test_funcs_and_constants_1(self):
        calc = Calculator(expression='pi+e')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(5.859874482048838, result)

    def test_funcs_and_constants_2(self):
        calc = Calculator(expression='sin(pi/2)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(1.0, result)

    def test_funcs_and_constants_3(self):
        calc = Calculator(expression='log(e)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(1.0, result)

    def test_funcs_and_constants_4(self):
        calc = Calculator(expression='log10(100)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(2.0, result)

    def test_funcs_and_constants_5(self):
        calc = Calculator(expression='sin(pi/2)*111*6')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(666.0, result)

    def test_funcs_and_constants_6(self):
        calc = Calculator(expression='2*sin(pi/2)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(2.0, result)

    def test_associative_1(self):
        calc = Calculator(expression='102%12%7')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(6, result)

    def test_associative_2(self):
        calc = Calculator(expression='100/4/3')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(8.333333333333334, result)

    def test_associative_3(self):
        calc = Calculator(expression='2^3^4')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(2417851639229258349412352, result)

    def test_comparison_1(self):
        calc = Calculator(expression='1+2*3==1+2*3')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(True, result)

    def test_comparison_2(self):
        calc = Calculator(expression='e^5>=e^5+1')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(False, result)

    def test_comparison_3(self):
        calc = Calculator(expression='1+2*4/3+1!=1+2*4/3+2')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(True, result)

    def test_common_1(self):
        calc = Calculator(expression='(100)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(100, result)

    def test_common_2(self):
        calc = Calculator(expression='666')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(666, result)

    def test_common_3(self):
        calc = Calculator(expression='10(2+1)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(30, result)

    def test_common_4(self):
        calc = Calculator(expression='-.1')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(-0.1, result)

    def test_common_5(self):
        calc = Calculator(expression='1/3')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(0.3333333333333333, result)

    def test_common_6(self):
        calc = Calculator(expression='1.0/3.0')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(0.3333333333333333, result)

    def test_common_7(self):
        calc = Calculator(expression='.1 * 2.0^56.0')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(7205759403792794.0, result)

    def test_common_8(self):
        calc = Calculator(expression='e^34')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(583461742527453.9, result)

    def test_common_9(self):
        calc = Calculator(expression='(2.0^(pi/pi+e/e+2.0^0.0))')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(8.0, result)

    def test_common_10(self):
        calc = Calculator(expression='sin(pi/2^1) + log(1*4+2^2+1, 3^2)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(2.0, result)

    def test_common_11(self):
        calc = Calculator(expression='(2.0^(pi/pi+e/e+2.0^0.0))^(1.0/3.0)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(2.0, result)

    def test_common_12(self):
        calc = Calculator(expression='10*e^0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(16.36381365110605, result)

    def test_common_13(self):
        calc = Calculator(expression='sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0^2.0))))--cos(1.0)--cos(0.0)^3.0)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(0.5361064001012783, result)

    def test_common_14(self):
        calc = Calculator(expression='2.0^(2.0^2.0*2.0^2.0)')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(65536.0, result)

    def test_common_15(self):
        calc = Calculator(expression='sin(e^log(e^e^sin(23.0),45.0) + cos(3.0+log10(e^-e)))')
        calc.prepare_expression()
        result = calc.calculate_result()
        self.assertEqual(0.76638122986603, result)







