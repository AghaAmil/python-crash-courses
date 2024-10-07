"""
Lesson 3 - Magic Methods and Operator Overloading
This course is complex, so some supplementary materials are provided to facilitate the learning process.

**Introducing Python Magic Methods**
https://www.datacamp.com/tutorial/introducing-python-magic-methods
https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/


**The whole OOP Lesson is useful**
https://www.programiz.com/python-programming/operator-overloading
https://www.geeksforgeeks.org/operator-overloading-in-python/

"""
import random


# An example magic method is __add__ for +

class Vectors:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vectors(self.x + other.x, self.y + other.y)


point_1 = Vectors(5, 4)
point_2 = Vectors(2, -3)
point_3 = Vectors(3, 4)

result = point_1 + point_2 + point_3

print(result.x)
print(result.y)

"""
The __add__ method allows for the definition of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.
"""

"""
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y). 
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 
There are equivalent r methods for all magic methods just mentioned.

"""


class SomeStrings:
    def __init__(self, some_string):
        self.some_string = some_string

    def __truediv__(self, other):
        line = '=' * len(other.some_string)
        return '\n'.join([self.some_string, line, other.some_string])


spam = SomeStrings('spam')
hello = SomeStrings('hello World!')

print(spam / hello)

"""
Python also provides magic methods for comparisons.

__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__. 
There are no other relationships between the other operators.

As you can see, you can define any custom behavior for the overloaded operators.
"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            res = other.cont[:index] + ">" + self.cont
            res += ">" + other.cont[index:]
            print(res)


spam = SpecialString("spam")
eggs = SpecialString("eggs")
var = spam > eggs

"""
There are several magic methods for making classes act like containers.

__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, 
and __int__, __str__, and the like, for converting objects to built-in types.
"""


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)


print('\nSome other examples.')

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
