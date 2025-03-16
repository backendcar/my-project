num = int(input("number: "))
compelet = True 

if num < 2:
    is_prime = False
      

else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("prime!")

else:
    print("not prime!")

# /////////////////////////


n = int(input("n: "))
r = int(input("r: "))

fact_n = 1
for i in range(1, n+1):
    fact_n = fact_n * i
print(fact_n)


fact_r = 1
for i in range(1, r+1):
    fact_r = fact_r * i
print(fact_r)


fact_n_r = 1
for i in range(1, n-r+1):
    fact_n_r *= i
print(fact_n_r)

# /////////////////////////


for num in range(2, 51):
    comp = True
    for i in range(2, num):
        if num % i == 0:
            comp = False
            break
    if comp:
        print(num)
        
# /////////////////////////

n = int(input("n: "))

a = 0
b = 1


if n <= 0:
    print("error!!!")

elif n == 1:
    print(a)
    
else:
    print(a)
    for i in range(1, n):
        
        c = a+b
        a = b
        b = c
        print(c)
        
# /////////////////////////
        
        
n = int(input("enter n: "))

fact = 1 

for i in range(1, n+1):
    fact = fact * i

print(fact)
        
    












