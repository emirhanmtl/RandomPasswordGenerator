import random

while True:

    print("Hello, Welcome to Password Generator 3000!")

    length = int(input("\nEnter the length of password: "))
    name = str(input("\nWhat is your password for:"))
    chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!'^+%&/()=?_->£#$½{[]}\|"

    password = ""


    for i in range(length):
        password += random.choice(chars)

    print("\nYour",name,"Password is:",password)
    print("\nYour password will be saved to password.txt")
    f = open("password.txt","a")
    f.write("\nYour "+name+" Password is: "+password)
    f.close()
    print("\nDo you want to generate new password ?")
    print("\nIf yes, enter 1.Else press any button.")
    a = (input())
    if (a=="1"):
        False
    else:
        quit()
