from attribute import GeneratorAttribute 
from numbers_functions import NumbersGeneratorFunctions as num_func
from string_functions import StringGeneratorFunctions as str_func
from generator import Generator
import sys

def attribute_test():
    settings = [105, 155, 1.5]
    salary = GeneratorAttribute(num_func.linear_values, settings)
    salary.run()
    print("[#] Test attr 1: ",salary.get_values())

    settings = [5, "float",105, 155]
    salary = GeneratorAttribute(num_func.array_values, settings)
    salary.run()
    print("[#] Test attr 2: ",salary.get_values())

def generator_test():
    SIZE = 30

    names_list = []
    attrs_list = []

    # Define Id Field
    settings = [0, SIZE, 1] 
    ids = GeneratorAttribute(num_func.linear_values, settings)
    # Add ID Field to generator
    names_list.append("ID")
    attrs_list.append(ids)

    # Define Name Field
    names = None

    with open("names.txt", mode = "r") as f:
        input = f.read().splitlines()
        names = GeneratorAttribute(str_func.array_string_reduce_size, [input, SIZE])
    # Add Name Field to generator
    names_list.append("names")
    attrs_list.append(names)

    # Define Grade Field
    settings = [SIZE, "float", 0, 10]
    grades = GeneratorAttribute(num_func.array_values, settings)
    # Add Grade Field to generator
    names_list.append("grade")
    attrs_list.append(grades)

    # Create the generator
    gen = Generator(names_list, attrs_list)

    # Define Age field and add directly to the generator
    gen.addField("Age", [SIZE, "int", 18, 40], num_func.array_values)

    # Create the generator
    gen = Generator(names_list, attrs_list)
    print("[#] Generator default format: ",gen.get_result())
    print("[#] Generator json: ",gen.get_json())
    print("[#] Generator csv: ")
    gen.get_csv(sys.stdout) # Print to console
    

if __name__ == '__main__':
    attribute_test()
    generator_test()