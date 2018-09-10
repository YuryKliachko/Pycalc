class Converter:
    def __init__(self):
        self.convertedList = []
    
    def validateOperand(self, operand: str):
        if '.' in operand and operand.count('.') == 1 and not operand.startswith('.') and not operand.endswith('.'):
            self.convertedList.append({'type': 'operand', 'value': float(operand)})
        elif '.' not in operand:
            self.convertedList.append({'type': 'operand', 'value': int(operand)})
        else:
            return Error(id=1, arg=operand)

    def validateOperator(self, operator: str):
        if operator in operators.keys():
            priority = operators[operator]['priority']
            self.convertedList.append({'type': 'operator', 'value': operator, 'priority': priority})
        else:
            return Error(id=2, arg=operator)

    def validateFunction(self, function: str):
        if function in functions.keys():
            self.convertedList.append({'type': 'function', 'value': function})
        else:
            return Error(id=3, arg=function)

    def convertToMath(self, tokenizedList):
        convertedList = []
        for item in tokenizedList:
            if item['type'] == 'operand':
                operand = self.validateOperand(item['value'])
                if isinstance(operand, Error):
                    return operand.raiseError()
            elif item['type'] is 'operator':
                operator = self.validateOperator(item['value'])
                if isinstance(operator, Error):
                    return operator.raiseError()
            elif item['type'] == 'function':
                function = self.validateFunction(item['value'])
                if isinstance(function, Error):
                    return function.raiseError()
            else:
                convertedList.append(item)
        return self.convertedList

conv = Converter()
print(conv.convertToMath([{'type': 'operator', 'value': '-'},
                          {'type': 'function', 'value': 'po'},
                          {'type': 'openingBracket', 'value': '('},
                          {'type': 'operand', 'value': '3.4'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operand', 'value': '5'},
                          {'type': 'closingBracket', 'value': ')'}]))
