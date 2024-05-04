class Car:
    def __init__(self,brand,model,color,year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def age(self):
        return 2024 - self.year
    def __str__(self):
        return self.brand + "," + self.model

obj1 = Car("pars","tu5","white",2020)
obj2 = Car("dena","plus","metalik",2021)
obj3 = Car("samand","LX","black",2022)

print(obj1)
print(obj2)
# print(obj3.age())