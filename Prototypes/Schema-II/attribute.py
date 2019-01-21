# Common Interface
class GeneratorAttribute:
    """
        This class will a create a dataset based on a generating function with her arguments (or settings)
        Fell free to use your own's function or use one predefined(eg: mumbers_function.py)
    """
    __values = None
    
    def __init__(self, generating_function, function_arguments):
        self.gen_func = generating_function
        self.func_args = function_arguments

    # generate the values
    def run(self):
        # call the generating functions and pass the her arguments
        self.__values = self.gen_func(*self.func_args)

    # return the generated values
    def get_values(self):
        # Check if the values has been generated, otherwise generate them
        if self.__values is None:
            self.run()
        return self.__values

    # return the size of 
    def get_size(self):
        # Check if the values has been generated, otherwise generate them
        if(self.__values is None):
                self.run()
        # Check if generating function has generate a list of values or single value
        if not isinstance(self.__values, list):
            return len(self.__values)
        # There is one value
        return 1

    