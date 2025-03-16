class Car:
    def __init__(self,model,color,year,mileage):
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
    
    def drive(self, distance):
        self.mileage += distance
        
    def display_info(self):
        print(f"model:{self.model}, color:{self.color}, year:{self.year}, mile:{self.mileage}")
        
car1 = Car("pars", "white", 1402, 1000)
car1.drive(500)
car1.display_info()