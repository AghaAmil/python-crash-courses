"""
You are making a video game! The given code declares a Player class, with its attributes and an intro() method.
Complete the code to take the name and level from user input, create a Player object with the corresponding values
and call the intro() method of that object.

Sample Input:
Tony
12

Sample Output:
Player: Tony - (Level 12)
"""


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print('\n**************')
        print('Player: ' + self.name + ' - ' + '(Level ' + self.level + ')')
        print('**************')


player_name = input('Enter\'s the player name: ')
player_level = (input('Enter\'s the player level: '))

gamer_1 = Player(player_name, player_level)
gamer_1.intro()

"""
You are making a drawing application, which has a Shape base class.
The given code defines a Rectangle class, creates a Rectangle object and calls its area() and perimeter() methods.
Do the following to complete the program:
1. Inherit the Rectangle class from Shape.
2. Define the perimeter() method in the Rectangle class, printing the perimeter of the rectangle.
"""


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)


class Rectangle(Shape):
    def perimeter(self):
        print(2 * (self.width + self.height))


shape_width = int(input('\nEnter the width of the shape: '))
shape_height = int(input('Enter the height of the shape: '))

shape_num_1 = Rectangle(shape_width, shape_height)
shape_num_1.area()
shape_num_1.perimeter()
