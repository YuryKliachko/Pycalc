errors = {1: lambda operand: 'ERROR: Typo in the operand {}!'.format(operand),
          2: lambda operator: 'ERROR: Unsupported operator {}!'.format(operator),
          3: lambda function: 'ERROR: Unsupported function {}!'.format(function),
          4: lambda bracket: 'ERROR: Opening {} bracket required!'.format(bracket),
          5: lambda bracket: 'ERROR: Closing {} bracket required!'.format(bracket),
          6: lambda operator: 'ERROR: Operand for {} required!'.format(operator),
          7: lambda operator: 'ERROR: negative number cannot be raised ({}) to a fractional power'.format(operator),
          8: lambda operator: 'ERROR: you cannot divide ({}) by zero!'.format(operator),
          9: 'ERROR: expression cannot be empty',
          10: lambda  operand: 'ERROR: operator for {} required!'.format(operand)}


class Error(Exception):
    def __init__(self, id, arg=None):
        self.arg = arg
        self.id = id
        if self.arg is not  None:
            self.text = errors[self.id](self.arg)
        else:
            self.text = errors[self.id]
        raise self
