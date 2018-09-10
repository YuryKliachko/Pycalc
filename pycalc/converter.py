class Converter:
    def convertToMath(self, tokenizedList):
        convertedList = []
        for item in tokenizedList:
            if item['type'] == 'operand':
                if '.' in item['value'] and not item['value'].startswith('.') and not item['value'].endswith('.'):
                    convertedList.append({'type': item['type'], 'value': float(item['value'])})
                elif '.' not in item['value']:
                    convertedList.append({'type': item['type'], 'value': int(item['value'])})
                else:
                    return 'Typo in the operand {}!'.format(item['value'])
            elif item['type'] is 'operator':
                if item['value'] in operators.keys():
                    priority = operators[item['value']]['priority']
                    convertedList.append({'type': item['type'], 'value': item['value'], 'priority': priority})
                else:
                    return 'Unsuported operator {}'.format(item['value'])
            elif item['type'] == 'function':
                if item['value'] in functions.keys():
                    convertedList.append({'type': item['type'], 'value': item['value']})
                else:
                    return 'Unsuported function {}'.format(item['value'])
            else:
                convertedList.append(item)

        return convertedList

conv = Converter()
print(conv.convertToMath([{'type': 'operator', 'value': '-'},
                          {'type': 'function', 'value': 'pow'},
                          {'type': 'openingBracket', 'value': '('},
                          {'type': 'operand', 'value': '0.34'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operator', 'value': '+'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operator', 'value': '-'},
                          {'type': 'operand', 'value': '5'},
                          {'type': 'closingBracket', 'value': ')'}]))