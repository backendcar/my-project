# چاپ اعداد کامل بین 1 تا 30 با)(for)

for num in range (2, 30):
    sum = 0
    for i in range (1, num-1):
        if num % i == 0:
            sum += i
    if sum == num :
        print(num)

