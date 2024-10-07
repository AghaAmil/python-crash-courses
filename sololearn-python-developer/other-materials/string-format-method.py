"""
In order to fully understand some Sololearn examples, you need to know the string format() method which has not been
explained in the sololearn course. You can use the article blow:

https://www.geeksforgeeks.org/python-string-format-method/
"""

# Let's learn the string format() method
person_name = 'Amirhossein'
person_age = 30

message = ('My name is {0}. I am {1} years old. \
My favorite number is {1}').format(person_name, person_age)

print(message)

# using a nice example of string format method
# take a precise look at how below code is written
txt = 'I have {num:.2f} dollars'
print(txt.format(num=100))

# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}".format("one", "two", "three", "four"))

"""
The basics of string format method is represented, the comprehensive information is provided in the above link
"""
