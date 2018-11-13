from generator import Generator
import random
import sys

def getNames(size):
    return ["Name " + str(i) for i in range(size)]

def getAges(size, minAge, maxAge):
    return [random.randint(minAge, maxAge) for i in range(size)]

if __name__ == '__main__':
    myDataGenerator = Generator()
    myDataGenerator.addField("ID", [0, 10], lambda X_min, X_max : [x for x in range(X_min, X_max)])
    myDataGenerator.addField("Name", [10], getNames)
    myDataGenerator.addField("Age", [10, 10, 30], getAges)
    myDataGenerator.get_csv(sys.stdout)