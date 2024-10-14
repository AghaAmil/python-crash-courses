"""
A class can be derived from more than one superclass in Python. This is called multiple inheritance.
"""


class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")


class Bat(Mammal, WingedAnimal):
    pass


# create an object of Bat class
animal_1 = Bat()
animal_1.mammal_info()
animal_1.winged_animal_info()

# blank line
print()


class SuperClass:

    def super_method(self):
        print("Super Class method called")


# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")


# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"
d2.derived1_method()  # Output: "Derived class 1 method called"
d2.derived2_method()  # Output: "Derived class 2 method called"

"""
If two superclasses have the same method (function) name and the derived class calls that method,
Python uses the MRO to search for the right method to call. 
"""


class SuperClass1:
    def info(self):
        print("Super Class 1 method called")


class SuperClass2:
    def info(self):
        print("Super Class 2 method called")


class Derived(SuperClass1, SuperClass2):
    pass


d1 = Derived()
d1.info()

# Output: "Super Class 1 method called"
