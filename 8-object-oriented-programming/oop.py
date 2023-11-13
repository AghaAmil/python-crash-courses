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
print('\nThe object dog has two attributes. Color: ', dog.color, ' and Age: ', dog.age)
print('The object cat has two attributes. Color: ', cat.color, ' and Age: ', cat.age)

# calling the animal sound
dog.dog_sound()
