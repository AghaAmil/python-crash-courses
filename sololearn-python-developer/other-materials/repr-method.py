"""
repr Magic Method

https://www.geeksforgeeks.org/python-__repr__-magic-method/

"""

"""
Syntax: object.__repr__()

object: The object whose printable representation is to be returned.
Return: Simple string representation of the passed object.
"""


# Python __repr__() method Example
class FML:
    def __init__(self, f_name, m_name, l_name):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name

    def __repr__(self):
        return f'<full_name Object contains {self.f_name} - {self.m_name} - {self.l_name}>'


full_name = FML('Amirhossein', 'Masoud', 'Moravveji')
print(repr(full_name))

print('\n')


# Difference between __str__() and __repr__() magic method
class UserName:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f'The User {self.username} entered the system'

    def __repr__(self):
        return f'UserName(username={self.username})'


user1 = UserName('kecy1amr')
print(user1.__str__())
print(user1.__repr__())
