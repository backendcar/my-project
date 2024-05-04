# lambda argument : expression

# x = lambda a : a * 3
# print(x(5))
# print(x(2))

def mySqrt(n):
    return lambda x : x ** (1/n)

sqrt2 = mySqrt(2)
sqrt3 = mySqrt(3)

print(sqrt2(4))
print(sqrt3(8))