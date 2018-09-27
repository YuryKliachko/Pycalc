from unittest import TestCase
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

    def test_validate_operator(self):
        self.fail()

    def test_validate_function(self):
        self.fail()

    def test_validate_bracket(self):
        self.fail()

    def test_convert_to_math(self):
        self.fail()
