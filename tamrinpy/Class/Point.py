class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point with x : {self.x} and y : {self.y}"