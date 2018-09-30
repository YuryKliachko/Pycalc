import math


class FunctionsManager:
    functions_dict = {'pow': pow, 'abs': abs, 'round': round}
    functions_dict.update(math.__dict__)

    @staticmethod
    def is_valid_function(function):
        if function in FunctionsManager.functions_dict.keys():
            return True
        else:
            return False

    @staticmethod
    def fetch_function_value(function):
        value = FunctionsManager.functions_dict[function]
        return value

    @staticmethod
    def add_new_dict(dictionary: dict):
        FunctionsManager.functions_dict.update(dictionary)