import random

class StringGeneratorFunctions:
    """
        Here are some predefined function for generating strings
    """

    # Get a random string from an input list
    @staticmethod
    def single_string(input):
        # Make sure that the input is a list
        input = list(input)
        size = len(input)
        return input[random.randint(0, size)]
    
    @staticmethod
    def array_string_reduce_size(input, reduce_to_size):
        # Make sure that the input is a list
        input = list(input)
        size = len(input)
        if(size > reduce_to_size):
            return input[:reduce_to_size]
        return input

    
