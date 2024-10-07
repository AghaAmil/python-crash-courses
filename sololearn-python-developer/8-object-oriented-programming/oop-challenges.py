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

"""
We are improving our drawing application.
Our application needs to support adding and comparing two Shape objects.
Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.
The addition should return a new object with the sum of the widths and heights of the operands, while the comparison
should return the result of comparing the areas of the objects.
"""


class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    # your code goes here
    def __add__(self, other):
        return Shape(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()


w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(
    '\nThe given code creates two Shape objects from user input, outputs the area() of their addition and compares '
    'them.')
print(result.area())
print(s1 > s2)

"""
We are working on a game. Our Player class has name and private _lives attributes. The hit() method should
decrease the lives of the player by 1. In case the lives equal to 0, it should output "Game Over". Complete the hit()
method to make the program work as expected.
"""


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1

        if self._lives == 0:
            print('Game Over')


p1 = Player('Cyberpunk77', 3)

p1.hit()
p1.hit()

print(p1.name, p1._lives)

p1.hit()

print('')
"""
The given code takes 2 numbers as input and calls the static area() method of the Shape class, to output the area
of the shape, which is equal to the height multiplied by the width. To make the code work, you need to define the
Shape class, and the static area() method, which should return the multiplication of its two arguments.
"""


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width * height


w = int(input('Enter the width of the shape: '))
h = int(input('Enter the height of the shape: '))

print(Shape.area(w, h))

"""
We are improving our game and need to add an isAlive property, which returns True if the lives count is greater than 0.
Complete the code by adding the isAlive property.
"""


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1

    # your code goes here
    @property
    def isAlive(self):
        if self._lives > 0:
            return True


p = Player("Cyberpunk77", int(input()))
i = 1
while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break
