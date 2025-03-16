class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grade = []
        
    def add_grade(self, grade):
        self.grade.append(grade)
        
    def avrrage(self):
        if len(self.grade) > 0:
            return sum(self.grade)/len(self.grade)
        else:
            return 0
        
            
student1=Student("Reza",12)
student1.add_grade(18)
student1.add_grade(20)
student1.add_grade(16)
print(student1.name)
print(student1.grade)
print(student1.avrrage())
            