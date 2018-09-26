from pycalc.tokenizer import Tokenizer
from pycalc.converter import Converter
from pycalc.error import Error
from pycalc.operator_stack import OperatorStack
from pycalc.operand_stack import OperandStack
from pycalc.item import Item


class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.tokenizer = Tokenizer()
        self.converter = Converter()
        self.prepared = []
        self.operand_stack = OperandStack()
        self.operator_stack = OperatorStack()
        self.current_operator = None

    def is_returned_as_error(self, item):
        if isinstance(item, Error):
            return True
        else:
            return False

    def calculate_on_stack(self):
        operator_on_stack = self.operator_stack.last_item
        if operator_on_stack.type == 'function':
            operators_function = operator_on_stack.function
            arguments = self.operand_stack.remove_args_from_stack(operator_on_stack.index)
            current_result = operators_function(*arguments)
        elif operator_on_stack.type == 'operator':
            operators_function = operator_on_stack.function
            first_operand = self.operand_stack.remove_pre_last_item_from_stack()
            second_operand = self.operand_stack.remove_last_item_from_stack()
            if first_operand is None:
                if operator_on_stack.value in ['+', '-']:
                    first_operand = Item(type='operand', value=0, index=self.current_operator.index)
                else:
                    return Error(id=6, arg=operator_on_stack.value)
            elif second_operand is None:
                if operator_on_stack.type != 'function':
                    return Error(id=6, arg=operator_on_stack.value)
            current_result = operators_function(first_operand.value, second_operand.value)
        else:
            current_result = self.operand_stack.last_item.value
            return current_result
        self.operator_stack.remove_last_item_from_stack()
        self.operand_stack.put_on_stack(Item(type='operand', value=current_result, index=self.current_operator.index), self.operator_stack)
        if self.operator_stack.is_empty() is False:
            if self.current_operator.priority >= self.operator_stack.last_item.priority:
                current_result = self.calculate_on_stack()
        return current_result

    def prepare_expression(self):
        tokenized = self.tokenizer.tokenize_expression(self.expression)
        converted = self.converter.convert_to_math(tokenized)
        self.prepared = converted

    def calculate_result(self):
        for item in self.prepared:
            if item.type == 'operand':
                self.operand_stack.put_on_stack(item, self.operator_stack)
            elif item.type == 'operator' or item.type == 'function':
                self.current_operator = item
                if self.operator_stack.is_empty():
                    self.operator_stack.put_on_stack(item, self.operand_stack)
                else:
                    if self.current_operator.priority < self.operator_stack.last_item.priority or self.current_operator.value == '^' and self.operator_stack.last_item.value == '^':
                        self.operator_stack.put_on_stack(item, self.operand_stack)
                    else:
                        self.calculate_on_stack()
                        self.operator_stack.put_on_stack(self.current_operator, self.operand_stack)
            elif item.type == 'opening_bracket':
                self.operator_stack.put_on_stack(item, self.operand_stack)
            else:
                for i in range(self.operator_stack.length):
                    self.calculate_on_stack()
                    if self.operator_stack.last_item.type == 'opening_bracket':
                        self.operator_stack.remove_last_item_from_stack()
                        break
        if self.operator_stack.is_empty():
            current_result = self.operand_stack.last_item.value
            return current_result
        elif self.operator_stack.length == 1:
            self.calculate_on_stack()
        for i in range(self.operator_stack.length):
            current_result = self.calculate_on_stack()
            if self.operator_stack.length == 0:
                return current_result
        return self.operand_stack.last_item.value

