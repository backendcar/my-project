class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def __repr__(self):
        return f"Color with red:{self.red} and green:{self.green} and blue:{self.blue}"

