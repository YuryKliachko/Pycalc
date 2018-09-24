from pycalc.operators_manager import OperatorsManager
from pycalc.functions_manager import FunctionsManager
from pycalc.error import Error
from pycalc.item import Item
from pycalc.operator_class import Operator
from pycalc.function import Function
from pycalc.bracket import Bracket


class Converter:
    def __init__(self):
        self.converted_list = []
        self.operator_manager = OperatorsManager()
        #self.functions_manager = FunctionsManager()
        self.level_of_enclosing = 0
        self.enclosing_required = False
        self.item_index = -1

    @property
    def previous_item(self):
        if len(self.converted_list) != 0:
            return self.converted_list[-1]
        else:
            return None
    
    def validate_operand(self, operand: str):
        if '.' in operand and operand.count('.') == 1:
            operand = float(operand)
        elif '.' not in operand:
            operand = int(operand)
        else:
            return Error(id=1, arg=operand)
        if self.previous_item is not None:
            if self.previous_item.type == 'closing_bracket':
                operator = '*'
                priority = self.operator_manager.fetch_operators_priority(operator)
                operator_function = self.operator_manager.fetch_operators_function(operator)
                self.converted_list.append(Operator(value=operator, index=self.item_index, function=operator_function, priority=priority))
        self.converted_list.append(Item(type='operand', value=operand, index=self.item_index))

    def validate_operator(self, operator: str):
        if self.operator_manager.is_valid_operator(operator):
            if self.previous_item is not None:
                if self.enclosing_required and self.previous_item.type != 'opening_bracket':
                    self.converted_list.append(Bracket(type='closing_bracket', value=')', index=self.item_index))
                    self.enclosing_required = False
                    self.item_index += 1
                if operator == '-' and self.previous_item.type == 'operator':
                    self.converted_list.append(Bracket(type='opening_bracket', value='(', index=self.item_index))
                    self.enclosing_required = True
                    self.item_index += 1
            else:
                if operator == '-':
                    self.converted_list.append(Bracket(type='opening_bracket', value='(', index=self.item_index))
                    self.enclosing_required = True
                    self.item_index += 1
            priority = self.operator_manager.fetch_operators_priority(operator)
            operator_function = self.operator_manager.fetch_operators_function(operator)
            self.converted_list.append(Operator(value=operator, index=self.item_index, function=operator_function, priority=priority))
        else:
            return Error(id=2, arg=operator)

    def validate_function(self, function: str):
        if FunctionsManager.is_valid_function(function):
            function_object = FunctionsManager.fetch_function_value(function)
            if isinstance(function_object, float) or isinstance(function_object, int):
                self.converted_list.append(Item(type='operand', value=function_object, index=self.item_index))
            else:
                self.converted_list.append(Function(value=function, index=self.item_index, function=function_object))
        else:
            return Error(id=3, arg=function)

    def validate_bracket(self, bracket):
        if bracket == '(':
            if self.previous_item is not None:
                if self.previous_item.type == 'operand':
                    if self.enclosing_required and self.previous_item.type != 'opening_bracket':
                        self.converted_list.append(Bracket(type='closing_bracket', value=')', index=self.item_index))
                        self.enclosing_required = False
                        self.item_index += 1
                    operator = '*'
                    priority = self.operator_manager.fetch_operators_priority(operator)
                    operator_function = self.operator_manager.fetch_operators_function(operator)
                    self.converted_list.append(Operator(value=operator, index=self.item_index, function=operator_function, priority=priority))
            self.converted_list.append(Bracket(type='opening_bracket', value=bracket, index=self.item_index))
            self.level_of_enclosing += 1
        elif bracket == ')':
            if self.level_of_enclosing > 0:
                self.level_of_enclosing -= 1
                self.converted_list.append(Bracket(type='closing_bracket', value=bracket, index=self.item_index))
            else:
                return Error(id=4, arg='(')

    def convert_to_math(self, tokenized_list):
        converted_list = []
        for item in tokenized_list:
            self.item_index += 1
            if item['type'] == 'operand':
                self.validate_operand(item['value'])
            elif item['type'] is 'operator':
                self.validate_operator(item['value'])
            elif item['type'] == 'function':
                self.validate_function(item['value'])
            elif item['type'] == 'opening_bracket' or item['type'] == 'closing_bracket':
                self.validate_bracket(item['value'])
            else:
                converted_list.append(item)
        if self.level_of_enclosing > 0:
            return Error(id=5, arg=')')
        else:
            if self.enclosing_required:
                self.converted_list.append(Bracket(type='closing_bracket', value=')', index=self.item_index))
            return self.converted_list

