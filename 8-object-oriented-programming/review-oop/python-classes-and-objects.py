"""
let's create and simple class
Then instantiating the class (creating a new object)
"""


class Dogs:
    # adding a simple attributes
    attr1 = 'mammal'
    attr2 = 'cute and fun'

    # adding a simple method
    def about(self):
        print(f'Dogs are {self.attr1} and they are {self.attr2}')


# creating an object
Rex = Dogs()

# display attributes
print(Rex.attr1)
print(Rex.attr2)

# call the class method
Rex.about()

# blank lines
print('\n')

"""
creating a more complex class with some input
"""


class EmployeeDetails:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

    def details(self):
        print('Representing the Employee Details')
        print('---------------------------------')
        print(f'Full Name: {self.name}')
        print(f'Employee ID: {self.id}')
        print(f'Email: {self.email}')


emp1 = EmployeeDetails('Amirhossein Moravveji', 12345, '<test@outlook.com>')
emp1.details()

# blank lines
print('\n')

"""
__str__ method
"""


class Fullname:
    def __init__(self, fist_name, last_name):
        self.first_name = fist_name
        self.last_name = last_name

    def __str__(self):
        return f'The logged in user\'s full name is {self.first_name} {self.last_name}'


print('Python has a particular method called __str__(). that is used to define how a class object should be '
      'represented as a string.')
print('-----------------------------------------------------------------------------------------------------'
      '------------------------')

user_1 = Fullname('Amirhossein', 'Moravveji')
print(user_1)

# blank lines
print('\n')

"""
Python3 program to show that the variables with a value assigned in the class declaration, are class variables and 
variables inside methods and constructors are instance variables.
"""


class Cats:
    # Class Variable
    animal = 'cat'

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color


# objects of the class Cats
Tom = Cats('Persian', 'grey')
Jess = Cats('Devon Rex', 'light brown')

print('Instance variables are for data, unique to each instance and class variables are for attributes and methods '
      'shared by all instances of the class.')
print('------------------------------------------------------------------------------------------------------------'
      '-------------------------------------')

print('Tom\'s Details')
print(f'Tom is a {Tom.animal}')
print(f'Tom is a {Tom.breed} {Tom.animal}')
print(f'Tom\'s color is {Tom.color}')

# a blank line
print('')

print('Jess\'s Details')
print(f'Jess is a {Jess.animal}')
print(f'Jess is a {Jess.breed} {Jess.animal}')
print(f'Jess\'s color is {Jess.color}')

# a blank line
print('')

# Class variables can be accessed using class
# name also
print(f'The details of {Cats.animal} are explained above.')

# blank lines
print('\n')

"""
Defining instance variables using the normal method:
Python3 program to show that we can create instance variables inside methods
"""


class Company:
    # class variable
    team = 'QA Team'

    def __init__(self, squad):
        # instance variable
        self.squad = squad

    # add an instance variable
    def employee_id(self, uid):
        self.uid = uid

    # retrieves the instance variable
    def show_id(self):
        return self.uid


print('Company Details:')
print(f'This is the {Company.team}')

c1 = Company('SnappClub')
c1.employee_id('#7724')

print(c1.squad)
print(c1.show_id())
