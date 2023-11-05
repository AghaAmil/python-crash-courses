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
