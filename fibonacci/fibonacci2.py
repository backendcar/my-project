def fibo(n):
    a = 0
    b = 1
    i = 0
    if n == 1 :
        return a
    elif n == 2 :
        return b
    elif n > 2 :
        
        while i < n :
            print(a)
            c = a + b
            a = b
            b = c 
            i += 1
        return c

print(fibo(8))
