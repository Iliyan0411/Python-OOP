import math


class Point2D:
    def __init__(self, x=0, y=0):
        'Initialize the position of point in 2D.'
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def print_point(self):
        print(f'({self.x}, {self.y})')




def main():
    p1 = Point2D(5, 4)
    p1.print_point()
    
    p1.reset() # == Point2D.reset(p1)
    p1.print_point()

    p2 = Point2D(1, 1)

    print(p1.distance(p2))
   
    p1.move(p2.x, p2.y)
    p1.print_point()


main()