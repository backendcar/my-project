from Point import Point
from color import Color


class Rectangle:
    def __init__(self, l, w, point , c):
        self.length = l
        self.width = w
        self.area_cal_counter = 0
        self.corner = point
        self.color = c

    def __repr__(self) -> str:
        return f"Rectangle with width:{self.width} and length:{self.length}"

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.perimeter() > other.perimeter()

    def area(self):
        self.area_cal_counter += 1
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area_factor(self, x):
        return self.area() * factor(x)


def factor(a):
    return a**2


def reducer(x):
    return x * 0.1

r1 = Rectangle(10,20, Point(0, 0, Color(1, 10, 100)), Color(10,20,30))
print(r1)
print(r1.corner)
print(r1.corner.color)
print(r1.color)

