num = int(input("number: "))
is_prime = True

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
        
            
    