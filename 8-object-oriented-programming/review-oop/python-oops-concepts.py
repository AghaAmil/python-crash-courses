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

print('\n')

"""
Inheritance in Python
"""

print('Python code to demonstrate how parent constructors are called')
print('-------------------------------------------------------------')


# parent class
class Person(object):

    # known as the constructor
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def display(self):
        print(self.name)
        print(self.uid)

    def details(self):
        print(f'User full name is {self.name}')
        print(f'User id is {self.uid}')


# child class
class Employee(Person):

    def __init__(self, name, uid, salary, position):
        self.salary = salary
        self.position = position

        # invoking the __init__ of the parent class
        Person.__init__(self, name, uid)

    def details(self):
        print('***The Employee Complete Details***')
        print(f'Employee name is {self.name}')
        print(f'Employee id is {self.uid}')
        print(f'Employee salary is ${self.salary}')
        print(f'Employee position is {self.position}')


emp1 = Employee('Amirhossein', '#6879', 2000, 'Software QA Engineer')
guest = Person('Ali Behnam', '#guest-1005')

emp1.display()
print('')
emp1.details()

print('')
guest.details()

print('\n')

"""
Polymorphism in Python
"""

print('This code demonstrates the concept of inheritance and method overriding in Python classes')
print('-----------------------------------------------------------------------------------------')


class Bird:

    def intro(self):
        print('There are many different types of bird in the world.')

    def flight(self):
        print('Most of the birds can fly while some cannot.')


class Sparrow(Bird):

    def flight(self):
        print('Sparrows can fly. They are smart, too.')


class Ostrich(Bird):

    def flight(self):
        print('Ostriches cannot fly. They are too fat.')


new_bird = Bird()
new_bird.intro()
new_bird.flight()

print('')

sparrow_1 = Sparrow()
sparrow_1.intro()
sparrow_1.flight()

print('')

ostrich_1 = Ostrich()
ostrich_1.intro()
ostrich_1.flight()

# blank lines
print('\n')

"""
Encapsulation in Python
"""

print('Encapsulation puts restrictions on accessing variables and methods directly and can prevent the accidental '
      'modification of data.')
print('-----------------------------------------------------------------------------------------------------------'
      '---------------------')


# creating a parent class with a private variable
class Base:

    def __init__(self):
        self.var1 = 'not a private variable'
        self.__var2 = 'private variable'

    @property
    def var2(self):
        return self._var2


# creating a child class
class Derived(Base):

    def __init__(self):
        # calling the constructor of the Base class
        Base.__init__(self)
        print('Calling the private variable of the Base class below:')
        print(self.__var2)


object_1 = Base()
print(object_1.var1)

# does not display the private variable
object_2 = Derived()

# will cause an error
# print(object_1.__var2)
