def fibo(n):
    a = 0
    b = 1
    if n == 1 :
        return 0
    elif n == 2 :
        return 1
    elif n > 2 :
        i = 2
        for i in range(2,n+1) :
            c = a + b
            a = b
            b = c
        return c
