"""
lesson 1 - Dictionaries
"""

ages = {
    'amir': 30,
    'shiva': 34,
    'fallah': 40
}

print(ages)
print(ages['amir'])
print(ages['fallah'])

car_info = {
    'brand': 'Porsche',
    'model': '911 Turbo S',
    'color': 'blue',
    'year': 2024
}

print('\nConsider the car info catalogue and enter a correct key to get the value.')
print(car_info)

car_key = input('\nEnter the key: ')

while not car_key in car_info:
    car_key = input('Please enter a correct key: ')

print(car_info[car_key])

"""
Lesson 2 - Dictionary Functions
"""

"""
Complete the program to take the country name as input and output its corresponding economic freedom rank.
In case the provided country name is not present in the data, output "Not found".
"""

country_data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

country = input('\nEnter the country\'s name: ')
print(country_data.get(country, 'Not found'))

"""
Lesson 3 - Tuples
"""

names = ('amir', 'ali', 'hasan', 'asgar')
names1 = 'akbar', 'asghar', 'ahmad', 'antar'  # without parentheses
names2 = 1, (1, 2, 3), 2, 3, 'pashm'  # nested tuples

print('')
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names1)
print(names2)

"""
You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the
contact. Complete the program to get a string as input, search for the name in the list of contacts and output the
age of the contact in the format presented below:

Sample Input
John

Sample Output
John is 31
"""

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

contact_name = input('\nEnter the name of the person in the contacts to get the details: ')
result = ''

for i in range(len(contacts)):
    if contact_name in contacts[i][0]:
        result = (str(contacts[i][0]) + ' is ' + str(contacts[i][1]))
        break
    else:
        result = "Not Found"

print(result)

"""
lesson 4 - Tuples Unpacking
"""

sample_numbers = (1, 2, 3)
A, B, C = sample_numbers
print('')
print(sample_numbers)
print(A)
print(B)
print(C)

x, y, z = [1, 2, 3]
print('\nValues x, y, z respectively:', x, y, z)

# unpacking and swapping numbers
x, y, z = y, z, x

print('\nValues x, y, z after swapping: ', x, y, z)

# Another modal of tuple unpacking
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('a is equal to: ', a)
print('b is equal to: ', b)
print('c is equal to: ', c)
print('d is equal to: ', d)

# having range for tuples unpacked
e, f, g, h, *i, j, k = range(20)
print('e is equal to: ', e)
print('f is equal to: ', f)
print('g is equal to: ', g)
print('h is equal to: ', h)
print('i is equal to: ', i)
print('j is equal to: ', j)
print('k is equal to: ', k)

"""
Tuples can be used to output multiple values from a function. You need to make a function called calc(), 
that will take the side length of a square as its argument and return the perimeter and area using a tuple. The 
perimeter is the sum of all sides, while the area is the square of the side length.

Sample Input
3

Sample Output
Perimeter: 12
Area: 9
"""


def calc(x):
    return x * 4, x ** 2


side = int(input("Enter the Square Dimension: "))
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))

"""
Lesson 5 - Sets
"""

sample_set = {1, 2, 3, 4, 5, 6}
print(sample_set)

print('3 in the set above is: ', 3 in sample_set)

# add and remove
print('\nAdd & Remove from above set.')
sample_set.add(7)
sample_set.remove(1)

print(sample_set)

# combine set using math operations
first_set = {1, 2, 3, 4, 5, 6}
second_set = {4, 5, 6, 7, 8, 9}

print('\nFirst set: ', first_set)
print('\nSecond set: ', second_set)

print('Union Operation using | of above sets: ', first_set | second_set)
print('Intersection Operation using & of above sets: ', first_set & second_set)
print('Difference Operation using - of above sets: ', first_set - second_set)
print('Symmetric Difference Operation using - of above sets: ', first_set ^ second_set)
