from random import *

user_password = input("Enter Your Password:")

password= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z',]

crack = ""

while (crack != user_password):
    crack = ""
    for i in range(len(user_password)):
        crack_letter = password[randint(0, 25)]
        crack += str(crack_letter)
    print(crack)

print("Your Password Is:",crack)