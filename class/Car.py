from Heater import Heater
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.heater = Heater()

    def break_(self):
        print(f"Khodro {self.model} tormoz kard.")

    def turnHeaterOn(self, temp=25):
        self.heater.on()
        self.heater.reachRequestedTemp(temp)

car1 = Car("Dena plus", 2024, "white")
car1.turnHeaterOn()




