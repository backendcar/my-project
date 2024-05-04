def isPrime(n):
    for i in range(2,int((n**0.5)) + 1):
        if n % i == 0 :
            return False
    return True

print(isPrime(23))

for j in range(1000,10000):
    if(isPrime(j)):
        print(j)
        # break