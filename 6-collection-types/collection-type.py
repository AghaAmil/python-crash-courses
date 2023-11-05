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

print('Consider the car info catalogue and enter a correct key to get the value.')
print(car_info)

car_key = input('Enter the key: ')

if car_key in car_info:
    print(car_info[car_key])
else:
    print('Please enter a correct key')

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

country = input('Enter the country\'s name: ')
print(country_data.get(country, 'Not found'))

"""
Lesson 3 - Tuples
"""

names = ('amir', 'ali', 'hasan', 'asgar')
names1 = 'akbar', 'asghar', 'ahmad', 'antar'  # without parentheses
names2 = 1, (1, 2, 3), 2, 3, 'pashm'  # nested tuples

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

contact_name = input('Enter the name of the person in the contacts to get the details: ')
result = ''

for i in range(len(contacts)):
    if contact_name in contacts[i][0]:
        result = (str(contacts[i][0]) + ' is ' + str(contacts[i][1]))
        break
    else:
        result = "Not Found"

print(result)
