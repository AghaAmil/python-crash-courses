"""
Properties
"""


class Pizza:
    def __init__(self, topping):
        self.topping = topping

    @property
    def pineapple_allowed(self):
        return False


dinner1 = Pizza(['cheese', 'tomato'])
print(dinner1.pineapple_allowed)


# dinner1.pineapple_allowed = True
# property 'pineapple_allowed' of 'Pizza' object has no setter

# setter & getter
class Sandwich:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self._cucumber_allowed = False

    @property
    def cucumber_allowed(self):
        return self._cucumber_allowed

    @cucumber_allowed.setter
    def cucumber_allowed(self, value):
        if value:
            password = input('Enter the password: ')
            if password == 'Kir khar':
                self._cucumber_allowed = value
            else:
                raise ValueError('You are not allowed to set a value!!')


meal_1 = Sandwich(['ham', 'cheese', 'lettuce'])
print(meal_1.cucumber_allowed)
meal_1.cucumber_allowed = True
print(meal_1.cucumber_allowed)



