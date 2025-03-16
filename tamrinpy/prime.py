# برنامه چاپ اعداد اول از 1 تا 50
# soal az chatgpt

for num in range(2, 51):  
    prime = True     # فرض اولیه برای اعداد اول( 
                     #فکر کنم به خاط دوتا شرطه)(prime = True) 
    for i in range(2, num):  #  از 2 یکی یکی اعداد وارد حلقه میشن
        if num % i == 0:    # ...در اینجا شرط اول بودنش بررسی میشه 
            prime = False    # اگه اول نباشه شرط نقض میشه و تموم میشه...
            break           
    if prime:               # اگه شرط اول بودن درست بود عدد چاپ میشه
        print(num)
        