# Dataset Generator

**A easy-to-use tool that helps you generate custom datasets**

**Motivation**: I needed a tool fro creating custom datasets in order to use on future projects that will involve working with Databases, Machine Learning.. 
    
**What the app does**: The program is a simple template, which, with a given generating function and her arguments will generate a dataset. The generating function can be a function that return a vector of int, float, string, etc. In this template is implemented 2 types of format outputs: JSON and CSV. 

## A Simple Example

#### Code
```python
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
```
#### Output
    ID,Name,Age
    0,Name 0,25
    1,Name 1,26
    2,Name 2,14
    3,Name 3,23
    4,Name 4,26
    5,Name 5,10
    6,Name 6,24
    7,Name 7,28
    8,Name 8,28
    9,Name 9,27

## Install

### Step 1
Clone the repository.
```sh
$ git clone https://github.com/Soare-Robert-Daniel/Project-Sarus
```
### Step 2
Install [python](https://www.python.org/).
### Step 3
Run the commands in terminal:
```sh
$ cd The-Beginning/Chapter-II/
$ python main.py
```
