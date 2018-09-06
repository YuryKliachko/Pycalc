'''
This class will be used for creating each new type of token when char type defined
'''
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value