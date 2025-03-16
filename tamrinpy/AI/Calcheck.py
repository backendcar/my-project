def calculation(target,num,*nums,operator = '+'):
    result = num
    if operator == '+':
        for item in nums:
            result += item
    elif operator == '-':
        for item in nums:
            result -= item
    else:
        print("ckoose between + and -")
    checker(target,result)   
    return result

def checker(target,result):
    if target<result:
        print("true target is graeter than you selected target!")
    elif target>result:
        print("true target is lower than you selected target!")
    else:
        print("your target is equal to our result!")

final_rasult = calculation(2,2,3,4)
print(final_rasult) 