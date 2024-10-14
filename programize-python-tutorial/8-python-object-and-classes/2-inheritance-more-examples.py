# Base class
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        return "This animal makes a sound."

    def __str__(self):
        return f"{self.name} is a {self.species}, aged {self.age}."


# Mammal subclass
class Mammal(Animal):
    def speak(self):
        return "This mammal makes a sound."

    def has_fur(self):
        return True


# Bird subclass
class Bird(Animal):
    def speak(self):
        return "This bird chirps."

    def can_fly(self, flight_ability=True):
        return flight_ability


# Dog subclass inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return "Woof!"


# Penguin subclass inheriting from Bird
class Penguin(Bird):
    def can_fly(self):
        return False


# Function to showcase the animals in the zoo
def zoo_showcase(animals):
    for animal in animals:
        print(animal.speak())
        if isinstance(animal, Mammal):
            print(f"This mammal has fur: {animal.has_fur()}")
        if isinstance(animal, Bird):
            print(f"Can this bird fly? {animal.can_fly()}")
        print(animal)  # Printing the details of the animal
        print("-" * 30)


# Example usage
dog = Dog(name="Buddy", species="Golden Retriever", age=3)
penguin = Penguin(name="Penny", species="Emperor Penguin", age=5)

zoo_showcase([dog, penguin])
