"""
List Characteristics
Lists are:

Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values.
"""

# empty list
empty_list = []

# list with different items
my_list = [1, 'hello', 5.4, {'type1': 'val1'}]

programming_languages = ['Python', 'Java', 'C++', 'Swift', 'Go', 'JavaScript', 'C#']
print(programming_languages)

print(programming_languages[0])
print(programming_languages[-1])
print(len(programming_languages))

# blank line
print()

# convert to list
my_string = 'Amirhossein Moravveji'
print(list(my_string))

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('List of Numbers=', list_of_numbers)
print('list_of_numbers[:5]=', list_of_numbers[:5])
print('list_of_numbers[10:]=', list_of_numbers[10:])
print('list_of_numbers[7:15]=', list_of_numbers[7:15])
print('list_of_numbers[2:18:2]=', list_of_numbers[1:18:2])
print('list_of_numbers[-1:-15:-2]=', list_of_numbers[-1:-15:-2])
print('list_of_numbers[-1]=', list_of_numbers[-1])

# blank line
print()

# Add Elements to a Python List
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

fruits.append('cherry')
print('Updated List:', fruits)

# Add Elements at the Specified Index
fruits.insert(2, 'cucumber')
print('Updated List:', fruits)

# Add Elements to a List From Other Iterables
sample_list = [2, 3, 4]
fruits.extend(sample_list)
print('Extended List:', fruits)

# blank line
print()

# change list items
colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

colors[2] = 'Blue'
print('Updated List:', colors)

# blank line
print()

# remove an item from a list
numbers = [2, 4, 7, 9]

numbers.remove(4)
print(numbers)

# blank line
print()

# iterate through a list
counter = 1

for items in programming_languages:
    print('Programming Language {}: {} '.format(counter, items))
    counter += 1
