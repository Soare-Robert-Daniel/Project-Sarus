import random
import numpy
class NumbersGeneratorFunctions:
    """
        Here are some predefined function for generating numbers
    """
    # Return a random value
    @staticmethod
    def single_value(value_type = "int", min_limit = 0, max_limit = 1):
        if(value_type == "int"):
            return random.randint(min_limit, max_limit)
        elif(value_type == "float" or value_type == "double"):
            return random.uniform(min_limit, max_limit)
        else:
            return 0
    
    # Return a list with random numbers
    @staticmethod
    def array_values(size = 10, value_type = "int", min_limit = 0, max_limit = 1):
        return [NumbersGeneratorFunctions.single_value(value_type, min_limit, max_limit) for i in range(size)]
    
    # Return a list with uniform numbers, based on a step [ x(i+1) = x(i) + step ] 
    @staticmethod
    def linear_values(min_limit = 0, max_limit = 1, step = 0.1):
        return list(numpy.arange(min_limit, max_limit, step))