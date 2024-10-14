"""
As we know, the + operator can perform addition on two numbers, merge two lists, or concatenate two strings.
With some tweaks, we can use the + operator to work with user-defined objects as well.
This feature in Python, which allows the same operator to have different meanings depending on the context is called operator overloading.
"""

number_1 = 5
number_2 = number_1.__add__(10)

print(number_2)

# blank line
print()


# Add Two Coordinates (Without Overloading)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add_points(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

p3 = p1.add_points(p2)

print((p3.x, p3.y))  # Output: (3, 5)


# Add Two Coordinates (With Overloading)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

# this statement calls the __add__() method
p3 = p1 + p2

print((p3.x, p3.y))  # Output: (3, 5)

# blank line
print()


# Overloading Comparison Operators
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age


p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False
