from pygments.lexer import words

list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension to create new list
doubled_value = [num * 2 for num in list_of_nums]

print(list_of_nums)
print(doubled_value)

squared_list = [num * num for num in list_of_nums]
print(squared_list)

# adding condition to list comprehension
conditional_value = [num * 2 for num in list_of_nums if num % 2 == 0]
print(conditional_value)

# blank line
print()

odd_numbers = [num for num in range(20) if num % 2 != 0]
print(odd_numbers)

# blank line
print()

# if...else With List Comprehension
even_odd_list = ['Even' if num % 2 == 0 else 'Odd' for num in list_of_nums]
print(even_odd_list)

# blank line
print()

# List Comprehension with String
sentence = 'Hello Python, My name is Amirhossein Moravveji'
vowels = 'aeiou'

result = [char for char in sentence.lower() if char in vowels]
print(result)

# blank line
print()

# Nested List Comprehension
multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]
print(multiplication)
