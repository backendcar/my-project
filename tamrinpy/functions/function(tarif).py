# types of functions

# 1.Built-in functions
print("Hello")

# 2.User-defined
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))


# 3.lambda
square = lambda x: x + x
print(square(4))


# 4.Recursive

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


# 5.Higher-Order

def apply_function(f, x):
    return f(x)

def sq(x):
    return x*x

print(apply_function(sq,5))

#6.built-in Higher-order


#7.default argument
def greet(name="Guest"):
    return f"Hello {name}!"

print(greet())
print(greet("Ali"))


#8.variable number of argument
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)


# 9.generator functions
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
        
counter = count_up_to(4)
for num in counter:
    print(num) 
    
    