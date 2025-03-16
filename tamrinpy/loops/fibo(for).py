n = int(input("number: "))

a = 0
b = 1
print(a)
# print(b)
for i in range(1,n):   # i ro az 1 ta n+1 mishmore miad
                       # chatgpt <-- (soal: chra be i gir ndad?!)(mishe c ro tarif nakard...
    
    c = a + b
    a = b
    b = c
    print(c) 