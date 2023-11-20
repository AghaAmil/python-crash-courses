"""
Class Methods
"""


# class method
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)


shape1 = Rectangle.square(10)
print('The area of the shape is', shape1.area())


# static method
class Pizza:
    def __init__(self, toppings):
        self.topping = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError('No Pineapples! ')
        else:
            return True


ingredients = ["cheese", "onions", "spam", 'sausage']
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
