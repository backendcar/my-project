
class Point:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.size = 1
        self.color = c

    def __repr__(self):
        return f"Point with x : {self.x} and y : {self.y}"

    def setSize(self, s):
        self.size = s