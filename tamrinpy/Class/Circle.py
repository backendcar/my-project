# 2. Calculating the area and circumference of a circle
# Create a class called Circle that has a radius property.
# Add two methods area() and circumference() that calculate the area and circumference of the circle, respectively.
# Create objects of this class and calculate the area and circumference of the circles.

class Circle:
    def __init__(self,radius): # ساخت متد برای شعاع
        self.radius = radius   
        
    def area(self): #مساحت
        return 3.14 * self.radius **2
        
    def circumference(self):
        return 2 * 3.14 * self.radius
    
# استفاده از کلاس 

circle1 = Circle(5)
print(circle1.area())
print(circle1.circumference())