#!/usr/bin/python3
"""
a class rectangle
##private instance, property setter, -width, must be an int or typeerror
a width < 0 or valueerror
##private instance - height, property setter, -height must be int or typeerror
height < 0 valueerror
##public instance - area that returns area, perimeter that returns perimeter
if width/height == = perimeter = 0
print()/str() prints # rectangle
if width/height ==0 return print()
repr return with eval()
"""


class Rectangle:
    """two private instances"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        square_area = self.__height * self.__width
        return square_area

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        p = 2*(self.__height + self.__width)
        return p

    def __str__(self):
        string = ""
        if self.area() == 0:
            return ""
        POUND = str(self.print_symbol)
        string = (self.__width * POUND for a in range(self.__height))
        lastString = '\n'.join(string)
        return (lastString)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
