class Converter:
    def convertToMath(self, tokenizedList):
        convertedList = []
        for item in tokenizedList:
            if item[0] == 'operand':
                if '.' in item[1] and not item[1].startswith('.') and not item[1].endswith('.'):
                    convertedList.append((item[0], float(item[1])))
                elif '.' not in item[1]:
                    convertedList.append((item[0], int(item[1])))
                else:
                    return f'Typo in the operand {item[1]}!'
            elif item[0] is 'operator':
                if item[1] in operators.keys():
                    convertedList.append((item[0], item[1]))
                else:
                    return f'Unsuported operator {item[1]}'
            elif item[0] == 'function':
                if item[1] in functions.keys():
                    convertedList.append((item[0], item[1]))
                else:
                    return f'Unsuported function {item[1]}'
            else:
                convertedList.append(item)

        return convertedList

conv = Converter()
print(conv.convertToMath([('operand', '+2'), ('openingBracket', '('), ('function', 'cos'), ('operator', '*'), ('operand', '1244.43244'), ('operator', '+'), ('openingBracket', '('), ('operand', '2'), ('operator', '+'), ('operand', '3'), ('closingBracket', ')'), ('closingBracket', ')')]))