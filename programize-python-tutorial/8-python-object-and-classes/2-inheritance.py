"""
Being an object-oriented language, Python supports class inheritance. It allows us to create a new class from an existing one.
The newly created class is known as the subclass (child or derived class).
The existing class from which the child class inherits is known as the superclass (parent or base class).
"""


class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is", self.name)

    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

# access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()
