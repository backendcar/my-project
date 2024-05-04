# def show(name):
#     return f"Hello {name.upper()}"

# for i in map(show,["amir","ali","hassan"]):
#     print(i)

# def show():
#     def shoot():
#         return "Hello"
#     return shoot()
# print(show())

# def show(name):
#     def shoot(n):
#         return f"Hello {n}!"
#     return shoot(name)
# print(show("Hossein"))


# def person(age):
#     def adult(name):
#         return f"{name} is Adult."
#     def kid(name):
#         return f"{name} is Kid."
    
#     if age >= 18 :
#         return adult
#     else:
#         return kid

# x = person(10)
# print(x("ali"))


# def person(age, name):
#     def adult():
#         return f"{name} is Adult."
#     def kid():
#         return f"{name} is Kid."
    
#     if age >= 18 :
#         return adult
#     else:
#         return kid

# x = person(20,"ali")
# print(x())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __call__(self, *args, **kwargs):
#          print(f"{self.name} is {self.age} years old.")


# p = Person("ali",20)
# p()


def show(name, *args, **kwargs):
    print(args)
    print(kwargs)
    return f"Hello {name}"

print(show("ali","hasan","hossei","reza", age = 20, height = 180))





