"""
A Python dictionary is a collection of items, similar to lists and tuples.
However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).
"""

country_capitals = {
    'Iran': 'Tehran',
    'England': 'London',
    'Japan': 'Tokyo',
    'Canada': 'Ottawa',
    'Germany': 'Berlin'
}

print(country_capitals)
print('Capital Of Iran:', country_capitals['Iran'])
print('Capital Of Germany:', country_capitals['Germany'])

# blank line
print()

# adding item to a dictionary
country_capitals['Italy'] = 'Rome'

print(country_capitals)
print('Capital Of Italy:', country_capitals['Italy'])

# blank line
print()

# remove dictionary items
del country_capitals['Italy']
print(country_capitals)

# blank line
print()

# change dictionary items
country_capitals['Italy'] = 'The Great Rome'
print(country_capitals)

# blank line
print()

# iterate through dictionaries
for country in country_capitals:
    print('Country:', country)
    print('Capital:', country_capitals[country])
    print()

# blank line
print()

for country, capital in country_capitals.items():
    print(f'Country: {country}, Capital: {capital}')

# blank line
print()

file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)  # Output: True
print(".mp3" in file_types)  # Output: False
print(".mp3" not in file_types)  # Output: True
