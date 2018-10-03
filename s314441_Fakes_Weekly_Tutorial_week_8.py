"""
Week 8 – Tutorials
Question 1
Write a Python class which has two methods get_String and
print_String. get_String accept a string from the user and print_String
print the string in upper case.

"""


class MyString:
    """
    Class to hold and manipulate a string.
    """
    def __init__(self):
        self.the_string = ""

    def __str__(self):
        return self.the_string

    def get_string(self):
        """ accepts a string from the user """
        self.the_string = input("Enter a string:")

    def print_string(self):
        """ returns the string in uppercase """
        print(self.the_string.upper())


x = MyString()
x.get_string()
x.print_string()

print(x)


"""
Question 2
Write a Python class named Rectangle constructed by a length and width
and a method which will compute the area of a rectangle.
"""
class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle class width of {self.width} and " \
               f"a length of {self.length}"

    def area(self):
        return self.length * self.width


x = Rectangle(10,5)
print(x.area())
print(x)

