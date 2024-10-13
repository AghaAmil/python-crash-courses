"""
Python Classes

A class is considered a blueprint of objects.
We can think of the class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows, etc.
Based on these descriptions, we build the house; the house is the object.
Since many houses can be made from the same description, we can create many objects from a class.
"""

"""
Python Objects

An object is called an instance of a class.
Suppose Bike is a class then we can create objects like bike1, bike2, etc from the class.
Here's the syntax to create an object.
"""


# Python Class and Objects
class StudentProfile:
    name = ''
    level = 0


student_1 = StudentProfile()
student_2 = StudentProfile()

student_1.name = 'Amirhossein'
student_1.level = 2

student_2.name = 'David'
student_2.level = 3

print(student_1)
print(f'Student Name: {student_1.name} // Level: {student_1.level}')
print(f'Student Name: {student_2.name} // Level: {student_2.level}')

# blank line
print()


# Python Methods
class Rectangle:
    width = 0
    height = 0

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


shape_1 = Rectangle()
shape_1.width = 15
shape_1.height = 25

print('Width: ', shape_1.width)
print('Height: ', shape_1.height)
print('Area: ', shape_1.area())
print('Perimeter: ', shape_1.perimeter())

# blank line
print()


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


user_1 = User('John', 2442)

print('User:', user_1.name)
print('UserID:', user_1.id)
