import os

print("A. Shutdown\nB. Restart\nC. Cancel")
choice = input("What is your choice? ")

if choice == 'A':
    print("Shutting down...")
    os.system("shutdown /s /t 3")

elif choice == 'B':
    print("restarting...")
    os.system("shutdown /r /t 3")

elif choice == 'C':
    print("Canceled!")
    exit()
else:
    print("Wrong Choice!!!")