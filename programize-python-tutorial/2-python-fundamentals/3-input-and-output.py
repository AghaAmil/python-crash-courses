# Python Output
from traceback import print_tb

print('Hello World! My name is ...')
print('Amirhossein Moravveji')

# print blank line
print()

# Python print() with end Parameter
print('This is the first paragraph', end=' ')
print('This is the second paragraph')

print('TEXT ONE', end='***')
print('TEXT TWO', end='***')
print('TEXT THREE')

# print blank line
print()

# Python print() with sep parameter
print('Amirhossein Moravveji', 1993, 'Senior Software Engineer', sep=' || ')

# print blank line
print()

# Print Concatenated Strings
print('This is a string ' + 'that connected to another string')

# print blank line
print()

year_born = 1993
print('I was born in ' + str(year_born) + ' years')

# print blank line
print()

# Output formatting
number_x = 10
number_y = 20

print('The number X = {} and the number Y = {}'.format(number_x, number_y))

# print blank line
print()

# Python Input
input_number = input('Enter a number: ')

print('Value: ', input_number)
print('Data Type: ', type(input_number))

# change the input type

# print blank line
print()

another_input_number = int(input('Enter another number: '))

print('Value: ', another_input_number)
print('Data Type: ', type(another_input_number))
