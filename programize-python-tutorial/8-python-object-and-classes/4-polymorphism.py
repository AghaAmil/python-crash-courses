"""
The literal meaning of polymorphism is the condition of occurrence in different forms.

Polymorphism is a very important concept in programming.
It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
"""

# Polymorphism in addition operator
num1 = 1
num2 = 2
print(num1 + num2)

str1 = 'Python'
str2 = 'Programming'
print(str1 + " " + str2)

# Polymorphic len() function
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

# blank line
print()


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'My name is {self.name} and I\'m {self.age} years old.')

    def speak(self):
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'My name is {self.name} and I\'m {self.age} years old.')

    def speak(self):
        print('Bark')


cat1 = Cat('John', 12)
dog1 = Dog('Max', 8)

for animals in (cat1, dog1):
    animals.speak()
    animals.info()
    animals.speak()

# blank line
print()

"""
However, notice that we have not created a common superclass or linked the classes together in any way.
Even then, we can pack these two different objects into a tuple and iterate through it using a common animal variable.
It is possible due to polymorphism.
"""

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
