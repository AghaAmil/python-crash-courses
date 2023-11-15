"""
Lesson 1 - Classes
"""


# the class (object builder in fact)
class Animal:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def dog_sound(self):
        print('Wooof!')


# creating instance of objects
dog = Animal('black & white', 7)
cat = Animal('light brown', 5)
bird = Animal('light yellow', 3)

# let's see how the created object looks like: (tell you sth in advance, it's not like what you expect)
print(dog)
print(cat)
print(bird)

# this is how you call it
print('\nThe object dog has two attributes. Color:', dog.color, 'and Age:', dog.age)
print('The object cat has two attributes. Color:', cat.color, 'and Age:', cat.age)

# calling the animal sound
dog.dog_sound()

"""
Lesson 2 - Inheritance
"""


# using the class above for inheritance
class Cat(Animal):
    def cat_sound(self):
        print('Meowwwww!')


class Bird(Animal):
    def bird_sound(self):
        print('Queedleeee!')


# inherit from the class above
tom = Cat('light grey', 10)
print('\nTom is a beautiful cat. it\'s color is', tom.color, 'and it\'s years', tom.age, 'old')
tom.cat_sound()

"""
Some Notes:

A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods, it overrides them. 
"""


class Wolf:
    def __init__(self, location, age):
        self.location = location
        self.age = age

    def bark(self):
        print('Woof!')


# override the method in wolf
class Huskey(Wolf):
    def bark(self):
        print('Awooooo!')


num1_huskey = Huskey('North Jungles', 12)
print('\nHuskers live in', num1_huskey.location, 'This beautiful one here is', num1_huskey.age, 'years old')
num1_huskey.bark()

print('\nThe function super is a useful inheritance-related function that refers to the parent class. ')


# inheritance-related functions
class Super:
    def func1(self):
        print('Function One')


class SubClass(Super):
    def func2(self):
        print('Function Two')
        super().func1()


SubClass().func2()

"""
Lesson 4 - Data Hiding
"""
