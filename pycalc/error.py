errors = {1: lambda operand: 'Typo in the operand {}!'.format(operand),
          2: lambda operator: 'Unsuported operator {}!'.format(operator),
          3: lambda function: 'Unsuported function {}!'.format(function),
          4: lambda bracket: 'Opening {} bracket required!'.format(bracket),
          5: lambda bracket: 'Closing {} bracket required!'.format(bracket),
          6: lambda operator: 'Operand next to {} required!'.format(operator)}
class Error:
    def __init__(self, id, arg=None):
        self.arg = arg
        self.id = id
        self.text = errors[self.id](self.arg)

    def raiseError(self):
        return self.text