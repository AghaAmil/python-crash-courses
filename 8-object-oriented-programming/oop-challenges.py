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
