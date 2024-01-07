"""
Creating a class and object with class and instance attributes
Overall concepts of OOP
"""
print('Creating a class and object with class and instance attributes')
print('--------------------------------------------------------------')


class Dog:
    # class attribute
    attr1 = 'mammal'

    # instance attribute
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name} is barking!')


# Object instantiation
Rex = Dog('Rex')
Tom = Dog('Tom')

# accessing class attributes
print(f'Rex is a {Rex.__class__.attr1}')
print(f'Tom is a {Tom.__class__.attr1}')

# accessing instance attribute
print(f'This dog name is {Rex.name}')
print(f'This dog is {Tom.name}')

# printing a blank line
print('')

# calling the class method
Rex.bark()
Tom.bark()


