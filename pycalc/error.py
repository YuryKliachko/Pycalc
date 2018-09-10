errors = {1: lambda operand: 'Typo in the operand {}!'.format(operand),
          2: lambda operator: 'Unsuported operator {}!'.format(operator),
          3: lambda function: 'Unsuported function {}!'.format(function)}
class Error:
    def __init__(self, id, arg):
        self.arg = arg
        self.id = id
        self.text = errors[self.id](self.arg)

    def raiseError(self):
        return self.text