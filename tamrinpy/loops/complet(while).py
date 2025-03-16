num = 2

while num < 50:
    # num += 1  ?!
    sumof = 0  #?!
    i = 1      #?!
    while i < num:
        if num % i ==0:
            sumof = sumof + i
        i = i+1 #?!...
    
    if sumof == num:
        print(num)
    num +=1 #?! محل قرار گیری کجاها میتونه باشه و چرا (line 10, 14) chatgpt