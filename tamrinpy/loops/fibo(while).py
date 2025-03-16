n = int(input("number: "))

a = 0
b = 1
i = 1   # شمارنده برای حرکت در حلقه
print(a)
print(b)

while i < n:    
    
    i = i + 1  #  (؟چرا؟)(!آخر حلقه هم میتونه بیاد) nاضافه شدن شمارنده تا رسیدن به 
    c = a + b   #  جمله بعدیه که حاصل جمع دوتای قبلیه (1+2=3 )(c)
    a = b       # jaye a, b miad(c = b + b)
    b = c       # jaye b dovomi, c = a+b miad (c = b + a+b)
    print(c)
    

    
    
    
    
     