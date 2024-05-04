def nameCheck():
    name = input("please enter your name: ")
    if name == "ashura" :
        print("welcome!")
    else:
        print("try again!")
        nameCheck()

nameCheck()

