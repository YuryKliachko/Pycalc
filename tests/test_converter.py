from unittest import TestCase
from pycalc.operator_class import Operator
from pycalc.converter import Converter
from pycalc.error import Error
from pycalc.bracket import Bracket
from pycalc.item import Item


class TestConverter(TestCase):
    def test_previous_item_positive(self):
        converter = Converter()
        test_object = {'object': 'test_object'}
        converter.converted_list.append(test_object)
        result = converter.previous_item
        self.assertEqual(test_object, result)

    def test_previous_item_negative(self):
        converter = Converter()
        result = converter.previous_item
        self.assertEqual(None, result)

    def test_validate_operand_integer(self):
        converter = Converter()
        operand = '666'
        converter.validate_operand(operand)
        last_item = converter.converted_list[-1]
        self.assertEqual('operand', last_item.type)
        self.assertEqual(666, last_item.value)

    def test_validate_operand_float(self):
        converter = Converter()
        operand = '11.22'
        converter.validate_operand(operand)
        last_item = converter.converted_list[-1]
        self.assertEqual('operand', last_item.type)
        self.assertEqual(11.22, last_item.value)

    def test_validate_operand_typo(self):
        converter = Converter()
        operand = '11.2.2'
        with self.assertRaises(Error):
            converter.validate_operand(operand)

    def test_validate_operand_add_multiplication_operator(self):
        converter = Converter()
        converter.converted_list.append(Bracket(type='closing_bracket', value=')', index=0))
        converter.validate_operand('1')
        last_item = converter.converted_list[-1]
        pre_last_item = converter.converted_list[-2]
        self.assertEqual(pre_last_item.type, 'operator')
        self.assertEqual(last_item.type, 'operand')

    def test_validate_operand_operator_missed(self):
        converter = Converter()
        operand = '1.5'
        converter.converted_list.append(Item(type='operand', value='1', index=0))
        with self.assertRaises(Error):
            converter.validate_operand(operand)

    def test_validate_operator_add_closing_bracket_before(self):
        converter = Converter()
        converter.converted_list.append(Item(type='operand', value='1', index=0))
        converter.enclosing_required = True
        converter.validate_operator('//')
        pre_last_item = converter.converted_list[-2]
        self.assertEqual(pre_last_item.type, 'closing_bracket')
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.value, '//')

    def test_validate_operator_add_opening_bracket_before(self):
        converter = Converter()
        converter.converted_list.append(Operator(value='/', index=2, function=None, priority=3))
        converter.validate_operator('-')
        pre_last_item = converter.converted_list[-2]
        self.assertEqual(pre_last_item.type, 'opening_bracket')
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.value, '-')

    def test_validate_operator_minus_the_first(self):
        converter = Converter()
        converter.validate_operator('-')
        pre_last_item = converter.converted_list[-2]
        self.assertEqual(pre_last_item.type, 'opening_bracket')
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.value, '-')
        self.assertEqual(converter.enclosing_required, True)

    def test_validate_operator_not_valid(self):
        converter = Converter()
        with self.assertRaises(Error):
            converter.validate_operator('~')

    def test_validate_function_is_constant(self):
        converter = Converter()
        function = 'e'
        converter.validate_function(function)
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.value, 2.718281828459045)
        self.assertEqual(last_item.type, 'operand')

    def test_validate_function_is_function(self):
        converter = Converter()
        function = 'cos'
        converter.validate_function(function)
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.type, 'function')

    def test_validate_function_not_valid(self):
        converter = Converter()
        function = 'sos'
        with self.assertRaises(Error):
            converter.validate_function(function)

    def test_validate_bracket_opening_bracket_the_first(self):
        converter = Converter()
        bracket = '('
        converter.validate_bracket(bracket)
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.type, 'opening_bracket')

    def test_validate_bracket_opening_bracket_add_multiplication_after_operand(self):
        converter = Converter()
        converter.converted_list.append(Item(type='operand', value='3', index=0))
        bracket = '('
        converter.validate_bracket(bracket)
        pre_last_item = converter.converted_list[-2]
        last_item = converter.converted_list[-1]
        self.assertEqual(pre_last_item.type, 'operator')
        self.assertEqual(last_item.type, 'opening_bracket')

    def test_validate_bracket_opening_bracket_add_multiplication_after_bracket(self):
        converter = Converter()
        converter.converted_list.append(Bracket(type='closing_bracket', value=')', index=0))
        bracket = '('
        converter.validate_bracket(bracket)
        pre_last_item = converter.converted_list[-2]
        last_item = converter.converted_list[-1]
        self.assertEqual(pre_last_item.type, 'operator')
        self.assertEqual(last_item.type, 'opening_bracket')

    def test_validate_bracket_closing_bracket_balanced(self):
        converter = Converter()
        converter.level_of_enclosing = 1
        converter.validate_bracket(')')
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.type, 'closing_bracket')

    def test_validate_bracket_closing_bracket_unbalanced(self):
        converter = Converter()
        with self.assertRaises(Error):
            converter.validate_bracket(')')

    def test_convert_to_math_coma(self):
        converter = Converter()
        tokenized_list = [{'type': 'coma', 'value': ','}]
        converter.convert_to_math(tokenized_list)
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.type, 'coma')

    def test_convert_to_math_closing_bracket_required(self):
        converter = Converter()
        tokenized_list = [{'type': 'opening_bracket', 'value': '('}]
        with self.assertRaises(Error):
            converter.convert_to_math(tokenized_list)

    def test_convert_to_math_add_closing_bracket(self):
        converter = Converter()
        tokenized_list = [{'type': 'operator', 'value': '-'}, {'type': 'operand', 'value': '2.5'}]
        converter.convert_to_math(tokenized_list)
        last_item = converter.converted_list[-1]
        self.assertEqual(last_item.type, 'closing_bracket')