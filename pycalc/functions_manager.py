import math


class FunctionsManager:
    """
    Functions manager will be used w/o instantiating in order to provide an access to it from main function in __main__
    module and from Converter class. I'm not sure it's a good idea, but it's the first one that I came up with :)
    """
    functions_dict = {'pow': pow, 'abs': abs, 'round': round}  # The main dictionary with func name as a key and
    functions_dict.update(math.__dict__) # function itself as a value. All dicts from user modules will be merged in it.

    @classmethod
    def is_valid_function(cls, function):
        """
        Checks if a function is valid. If yes, it returns True, otherwise False will be returned
        """
        if function in cls.functions_dict.keys():
            return True
        else:
            return False

    @classmethod
    def fetch_function_value(cls, function):
        """
        Retrieves and returns a function itself from the functions dictionary.
        """
        value = cls.functions_dict[function]
        return value

    @classmethod
    def add_new_dict(cls, dictionary: dict):
        """
        Merges a dictionary from a user's module in the main functions dictionary.
        """
        cls.functions_dict.update(dictionary)
