n = int(input("Enter n: "))
result = []

def fibo(n):
    if n<=1:
        return n
    
    else:
        result = result.append(fibo(n-1))
        return fibo(n-1) + fibo(n-2) 

fibo(n)
print(result)
    

  
 