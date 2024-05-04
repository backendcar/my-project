# def creat_add(x):
#     def add(y):
#         return x + y

#     return add

# add_2 = creat_add(2)
# print(add_2(10))


def hello_decorators(func):
    def inner1(*args,**kwargs):
        print("step one")

        res = func(*args,**kwargs)

        print("finall step")
        return res
    return inner1

@hello_decorators

def add(a,b,c):
    print("we are in add function")
    return a + b + c

@hello_decorators
def mul(a,b,c):
    print("we are in multiple")
    return a * b * c

print(add(4,5,6))
print(mul(2,3,4))
