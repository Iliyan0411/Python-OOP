from shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def parameter(self):
        return 2 * math.pi * self.radius

    def surface(self):
        return math.pi * self.radius**2

    def print_type(self):
        print('CIRCLE')


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def parameter(self):
        return 4 * self.side

    def surface(self):
        return self.side * self.side

    def print_type(self):
        print('SQUARE')
