"""
Data Hiding
"""


# Weakly private method
class NumsList:
    def __init__(self, content):
        self._hiddenContent = content

    def push(self, value):
        self._hiddenContent.insert(0, value)

    def pop(self):
        return self._hiddenContent.pop(-1)

    def __repr__(self):
        return f'NumsList({self._hiddenContent})'
        # The __repr__ magic method is used for string representation of the instance.


list1 = NumsList([1, 2, 3, 4])
print(list1)

list1.push(0)
print(list1)

list1.pop()
print(list1)

print(list1._hiddenContent)

print('')


# Strongly private methods
class UserID:
    __id = 7868

    def print_id(self):
        print(self.__id)


user1 = UserID()

user1.print_id()
print(user1._UserID__id)
