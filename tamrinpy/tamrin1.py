# print divisor
x = int(input("number: "))
divisor = []

for i in range(1, x+1):
    if x % i == 0:
        divisor.append(i)

print(divisor)
    
