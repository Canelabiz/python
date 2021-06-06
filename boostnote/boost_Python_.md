# Python

## Concept: Thruthiness

```python
False # false is false
[]    # empty lists / arrays are false
{}    # empty dictionaries are false
""    # empty strings are false
0     # zero ints are false
0.0   # zero floats are false
None  # None / null / nil / pointers are false

# trivial values are converted to false
# Everything else is true!
```

## Concept: for-in loop

for-in loops are the easiest, safest way to process a collection

```python
> items = ['cat','hat','mat']

> for item in items:
    print('The item is {}'.format(item))

The item is cat
The item is hat
The item is mat
```

enumerated for-in-loop

```python
> for (idx, item) in enumerate(items):
    print('Item {} is {}'.format(idx, item))

Item 0 is cat
Item 1 is hat
Item 2 is mat
```

##### return an index and the item via enumerate(collection)

## Concept: import

Modules must be imported before being used

```python
import os                 # retain namespace
from os import path       # get individual entities
from os import *          # import all direct

os.path.exists(filename)  # style 1
path.exists(filename)     # style 2
```

## Concept: file i/o

open creates a file stream
with adds auto-closing safety

```python
items = ['cat', 'hat', 'mat']

with open(filename, 'w') as fout:
  for e in items:
    fout.write(e + '\n')
```

file streams have many read / write operations

## Concept: Complex conditionals

```python
if not x and (z != 2 or not y):
  # if code here
```

Complex conditionals are created using not, and, and or

## Concept: Doc strings

```python
def some_method():
  """  
  some_method will book a hotel and 
  flight for the user in one shot.
  """

  # method implementation
```

A string with triple-quotes at the beginning of the method / class / module is a doc string

This description is used in generating docs and intellisense

## Concept:

```python
__name__
```

```python
# module.py
print('hello world, from {}'.format(__name__))

# __name__ is displayed here.
```

```python
# program.py
import module

# __name__ is displayed indirectly here.
```

output:

```python
> python ./module.py
hello world, from __main__

> python ./program.py
hello world, from module

# Depending on caller, __name__ is 'module' or is '__main__'
```

## Concept: slicing

slices are like array access, but for ranges

```python
# first nine prime numbers
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# array access examples
first_prime = nums[0]   # 2
last_prime = nums[-1]   # 23

# slice examples
lowest_four = nums[0:4] # [2, 3, 5 , 7]
lowest_four = nums[:4]  # [2, 3, 5 , 7]

Middle = nums[3:6]      # [7, 11, 13]

last_four = nums[5:9]   # [13,17,19,23]
last_four = nums[5:]    # [13,17,19,23]
last_four = nums[-4]    # [13,17,19,23]
```

## Concept: tuples

tuples group disparate types of data into one bound item.
The commas define the tuples

```python
m = (22.5, 44.234, 19.02, 'strong')
m = 22.5, 44.234, 19.02, 'strong'

temp = m[0]
quality = m[3]

print(m)
# (22.5, 44.234, 19.02, 'strong')

t, la, lo, q = m
# t=22.5, la=44.234, lo=19.02, q='strong')
```
Tuples can be unpacked back into single variables

## Concept: named tuples

named tuples are clerar and explicitly named
```python
Measurement = collections.namedtuple(
    'Measurement',
    'temp, lat, long, quality')
  
m = Measurement(22.5, 44.234, 19.02, 'strong')

temp = m[0] # is replaced by:
temp = m.temp
q = m.quality

print(m)
# Measurement(temp=22.5, lat=44.234, long=19.02, quality='strong')
```

## Concept: class structure

classes are defined with the [class] keyword

[self] is explicitly passed everywhere

[__init__] is the initializer and is where fields are defined

def defines methods on the classes (instance and static)

```python
class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def walk(self):
        print(f'{self.name}walks around')
```

## Concept: class vs objects

Classes are blueprints for creating objects

```python
class Creature:
    def __init__(self, power):
        # ...
        
    def walk(self):
        # ...
```

objects are created via Classes.
```python
squirrel = Creature(7)
dragon = Creature(50)

squirrel.walk()
dragon.walk()
```

## Concept: Inheritance

Dragon is a specialization of Creature
Indicated via class Type(BaseType) syntax

```python
class Dragon(creatire):

    def __init__(self, name, level, scale_thickness):
        super().__init__(name, level)
        self.scale_thickness = scale_thickness
    
    def breath_fire(): 
        # ...
```

## Concept: Polymorphism

All types derive from Creature
Share name and level in common

```python
creatures = [
    SmallAnimal('Toad', 1),
    SmallAnimal('Bat', 2),
    Creature('Tiger', 12,
    Dragon('Dragon', 50, 5),
    Wizard('Evil Wizard', 1000),
]

wizard = Wizard('Gandolf', 22)
for c in creatures:
    wizard.attack(c)
```

## Concept: Recursion

a recursive function calls itself with modified data

```python
def factorial(n):
    if n <=1:
        return 1
    
    return n * factorial(n - 1)
```

## Concept: Generator methods

```python
def fibonacci(limit):
    current = 0
    next = 1
    
    while current < limit:
        current, next = next, next + current
        yield current
```
After the item is returned and processed, execution returns and resumes

The yield keyword returns one element of a sequence
