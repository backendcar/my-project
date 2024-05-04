# 0,1,1,2,3,5,8,13,..., n+(n-1)
def fibo(n):
    a = 0
    b = 1
    if n == 1 :
        return a
    elif n == 2 :
        return b
    elif n > 2 :
        i = 2
        while i < n :
            c = a + b
            a = b
            b = c 
            i += 1
        return c

print(fibo(14))
