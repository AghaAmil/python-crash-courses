"""
A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
For instance, if we need to store information about student IDs, a set is suitable since student IDs cannot have duplicates.
"""

student_id = {110, 111, 112, 113, 114, 115}
print('Student ID:', student_id)

vowels_letters = {'a', 'i', 'u', 'o', 'e'}
print('Vowels letters:', vowels_letters)

mixed_items = {'python', 1, 2.2, -98, 'Bye'}
print('Mixed items:', mixed_items)

# blank line
print()

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))

# blank line
print()

# duplicate items in a set
random_set = {1, 1, 2, 3, 3, 3, 4, 5, 6, 6}
print('Random set:', random_set)

"""
Sets are mutable. However, since they are unordered, indexing has no meaning.
"""

# blank line
print()

numbers = {21, 34, 54, 12}
print('Initial Numbers:', numbers)

numbers.add(32)
print('Updated Numbers:', numbers)

# blank line
print()

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'Google', 'Apple']

# using update() method
companies.update(tech_companies)
print(companies)

# blank line
print()

languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

# blank line
print()

fruits = {"Apple", "Peach", "Mango", "Cucumber", 'Orange', 'Pineapple'}

# for loop to access each fruits
for fruit in fruits:
    print(fruit)
