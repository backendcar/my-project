from Point import Point
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.a = 0
        self.corner = Point(0,0)
        
    def __repr__(self) -> str:
        return f"Rectangle with length {self.length} and width {self.width}"
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def area(self):
        self.a += 1
        return self.length * self.width
    
    def pr(self):
        return 2 * (self.length + self.width)
    
    def area_factor(self, x):
        return self.area * factor(x)
    


def factor(a):
    return a**2

def reducer(rectangle):
    return rectangle.pr() * 0.1

r1 = Rectangle(10, 20)
print(r1)
print(r1.corner)