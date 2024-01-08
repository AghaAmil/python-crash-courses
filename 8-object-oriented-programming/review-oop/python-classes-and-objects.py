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

user_1 = Fullname('Amirhossein', 'Moravveji')
print(user_1)

# blank lines
print('\n')
