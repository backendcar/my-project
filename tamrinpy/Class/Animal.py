class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def speak(self):
        raise NotImplementedError("must interhais!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} say Woof!")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} say Meow!")
        

# animal = Animal("asb", "Horse")
dog = Dog("sag","Dog")
cat = Cat("gorbe","Cat")
dog.speak()
cat.speak()