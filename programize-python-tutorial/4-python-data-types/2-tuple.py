"""
A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is
created.

Tuple Characteristics
Tuples are:

Ordered - They maintain the order of elements.
Immutable - They cannot be changed after creation.
Allow duplicates - They can contain duplicate values.
"""

number = (1, 2, 3, 4, 5)
print(number)

# create a tuple using tuple constructor
tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor)
print('Tuple Length:', len(tuple_constructor))

empty_tuple = ()
sample_tuple = ('jack', 1, 2.3, [1, 2, 'Amir'])

print(empty_tuple)
print(sample_tuple)

# Access Items Using Index
languages = ('Python', 'Swift', 'C++')

print(languages[0])  # Python
print(languages[2])  # C++

# blank line
print()

for items in sample_tuple:
    print(items)
