"""
Iterators are methods that iterate collections like lists, tuples, etc.
Using an iterator method, we can loop through an object and return its elements.

Technically, a Python iterator object must implement two special methods, __iter__() and __next__(),
collectively called the iterator protocol.
"""
my_list = [3, 4, 5, 6]

iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))
# get the second element of the iterator
print(next(iterator))
# get the third element of the iterator
print(next(iterator))
# get the fourth element of the iterator
print(next(iterator))

# blank line
print()

my_second_list = [1, 2, 3, 4, 5]
iterator_2 = iter(my_second_list)

# another way to iterate
for items in iterator_2:
    print(items)

# blank line
print()


# Building Custom Iterators
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))  # prints 1
print(next(i))  # prints 2
print(next(i))  # prints 4
print(next(i))  # prints 8
print(next(i))  # raises StopIteration exception
