from unittest import TestCase
from pycalc.item import Item

class TestItem(TestCase):

    def test_item_object(self):
        test_type = 'operand'
        test_value = '9.999'
        test_index = 1
        item = Item(test_type, test_value, test_index)
        self.assertEqual(item.type, test_type)
        self.assertEqual(item.value, test_value)
        self.assertEqual(item.index,test_index)
