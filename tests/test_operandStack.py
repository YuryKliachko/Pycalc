from unittest import TestCase
from pycalc.operand_stack import OperandStack
from unittest.mock import MagicMock
from pycalc.operator_stack import OperatorStack
from pycalc.item import Item


class TestOperandStack(TestCase):
    def setUp(self):
        self.operand_stack = OperandStack()

    def test_put_on_stack_put_attribute(self):
        stack_to_refresh = OperatorStack()
        stack_to_refresh.is_function_on_stack = MagicMock(return_value=True)
        test_item = Item(type='operand', value='666', index=1)
        self.operand_stack.put_on_stack(test_item, stack_to_refresh)
        last_item = self.operand_stack.container[-1]
        self.assertEqual(last_item.type, 'argument')

    def test_put_on_stack_put_operand(self):
        stack_to_refresh = OperatorStack()
        stack_to_refresh.is_function_on_stack = MagicMock(return_value=False)
        test_item = Item(type='operand', value='666', index=1)
        self.operand_stack.put_on_stack(test_item, stack_to_refresh)
        last_item = self.operand_stack.container[-1]
        self.assertEqual(last_item.type, 'operand')


    def test_remove_pre_last_item_from_stack(self):
        test_item_1 = Item(type='operand', value='0.1', index=1)
        test_item_2 = Item(type='operand', value='0.2', index=2)
        self.operand_stack.container.append(test_item_1)
        self.operand_stack.container.append(test_item_2)
        removed_item = self.operand_stack.remove_pre_last_item_from_stack()
        self.assertEqual(removed_item, test_item_1)
        self.assertNotIn(test_item_1, self.operand_stack.container)
        self.assertIn(test_item_2, self.operand_stack.container)

    def test_remove_args_from_stack(self):
        test_item_1 = Item(type='argument', value='0.1', index=1)
        test_item_2 = Item(type='argument', value='0.2', index=2)
        self.operand_stack.container.append(test_item_1)
        self.operand_stack.container.append(test_item_2)
        arguments = (test_item_1.value, test_item_2.value)
        result = self.operand_stack.remove_arguments_from_stack(function_index=0)
        self.assertEqual(result, arguments)
        self.assertNotIn(test_item_1, self.operand_stack.container)
        self.assertNotIn(test_item_2, self.operand_stack.container)
