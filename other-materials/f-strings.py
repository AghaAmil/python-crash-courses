"""
f-string in Python

https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
"""
import datetime

# Python3 program introducing f-string
word = 'Geeks'
print(f'{word}for{word} is a portal for {word}.')

name = 'Amirhossein'
age = 30
print(f'\nMy name is {name} and I\'m {age} years old.')

# Prints today's date with help
# of datetime library
today = datetime.datetime.today()
print(f'\nToday is {today:%B %d, %y}')
print(f'Today is {today:%B %d, %Y}')
