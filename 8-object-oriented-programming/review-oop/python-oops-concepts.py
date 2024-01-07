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


