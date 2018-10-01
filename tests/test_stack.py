from unittest import TestCase
from pycalc.stack import Stack
from pycalc.item import Item
from pycalc.operator_stack import OperatorStack


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_length(self):
        test_item = Item('operand', 666, 1)
        self.stack.container.append(test_item)
        self.assertEqual(self.stack.length, 1)

    def test_is_empty_positive(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_empty_negative(self):
        test_item = Item('operand', 666, 1)
        self.stack.container.append(test_item)
        self.assertEqual(self.stack.is_empty(), False)

    def test_put_on_stack(self):
        stack_to_refresh = OperatorStack()
        test_item = Item('operand', 666, 1)
        self.stack.put_on_stack(test_item, stack_to_refresh)
        last_item = self.stack.container[-1]
        self.assertEqual(last_item, test_item)

    def test_last_item(self):
        test_item = Item('operand', 666, 1)
        self.stack.container.append(test_item)
        self.assertEqual(self.stack.last_item, test_item)

    def test_remove_last_item_from_stack_positive(self):
        test_item = Item('operand', 666, 1)
        self.stack.container.append(test_item)
        result = self.stack.remove_last_item_from_stack()
        self.assertNotIn(result, self.stack.container)
        self.assertEqual(result, test_item)

    def test_remove_last_item_from_stack_nagative(self):
        result = self.stack.remove_last_item_from_stack()
        self.assertEqual(result, None)


