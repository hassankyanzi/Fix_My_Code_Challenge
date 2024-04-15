#!/usr/bin/python3

class Square:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def width(self):
        """ Get the width of the square """
        return self._width

    @width.setter
    def width(self, value):
        """ Set the width of the square """
        self._width = value

    @property
    def height(self):
        """ Get the height of the square """
        return self._height

    @height.setter
    def height(self, value):
        """ Set the height of the square """
        self._height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Printable representation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Create a square object """
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
