def palindrome(number):
    print("original number", number)
    original_num = number

    reversed_num = 0
    while number > 0 :
        reminder = number % 10
        reversed_num = (reversed_num * 10) + reminder
        number = number // 10

    if original_num == reversed_num:
        print("palindrome")
    else:
        print("Not palindrome")

palindrome(12321)
palindrome(568)