my_name = 'Amirhossein Moravveji'
print(my_name)

# accessing string characters
print('Printing the first character:', my_name[0])
print('Printing the last character:', my_name[-1])
print('Printing the [3:10] characters:', my_name[3:10])
print('Printing the [1:8:2] characters:', my_name[1:8:2])

# blank line
print()

"""
In Python, strings are immutable. That means the characters of a string cannot be changed. For example,
"""

"""
message = 'Hola Amigos'
message[0] = 'H'
print(message)
"""

message = 'Hola Amigos'

# assign new string to message variable
message = 'Hello Friends'

print(message)  # prints "Hello Friends"

# blank line
print()

# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)

# blank line
print()

str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

# blank line
print()

greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

# blank line
print()

for char in my_name:
    if char != ' ':
        print('printing each character my name:', char)
    else:
        print('printing each character my name: "space character"')

# blank line
print()

print('a' in 'program')  # True
print('at' not in 'battle')  # False
