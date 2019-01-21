import attribute 
import json
import csv
from json_encoder import CustomEncoder

class Generator:
    """
        This class will run all generating functions from a list of attributes
        and will pair the result with his field's name. 
        
        In the a case of a CSV Format, a field is the columnn of the table 
    """
    __results = None

    def __init__(self, names_list = [], attributs_list = []):
        self.names = names_list 
        self.attrs = attributs_list
    
    # generate the values
    def gen(self):
        self.__results = {}
        for index in range(len(self.names)):
            # get the values from every attribute in the attres list
            self.__results[self.names[index]] = self.attrs[index].get_values()

    # create a field with a name and a attr
    def addFieldWithAttr(self, name, attr):
        self.names.append(name)
        self.attrs.append(attr)
    
    # create a field with a name, settings (or function's argumentes) and a function 
    def addField(self, name, settings, generating_function):
        # Create the atribute
        attr = attribute.GeneratorAttribute(generating_function, settings)
        # Add to the generator
        self.names.append(name)
        self.attrs.append(attr)
    
    # get the result in default format
    def get_result(self):
        # Check if the values has been generated, otherwise generate them
        if(self.__results is None):
            self.gen()
        return self.__results


    # get the result in JSON format
    def get_json(self):
        # Check if the values has been generated, otherwise generate them
        if(self.__results is None):
            self.gen()
        return json.dumps(self.__results, cls = CustomEncoder)

    # get the result in CVS format
    # the output can be a file name or the standard output
    def get_csv(self, output):
        # Check if the values has been generated, otherwise generate them
        if(self.__results is None):
            self.gen()
        
        # Attention, the row of the table will be equal with the smallest list's size of the arttrs list  
        size = min([ x.get_size() for x in self.attrs])

        # Create te writer, change the parameters if you want another format
        writer = csv.writer(output, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

        # Write the data to the output
        writer.writerow(self.names)
        for index in range(size):
            writer.writerow([ self.__results[name][index] for name in self.names])

        

