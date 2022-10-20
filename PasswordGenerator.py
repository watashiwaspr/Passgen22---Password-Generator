import string

import random
length = int(input("Password length(i prefer at least 16): "))

characters = ""
 
while(True):
    ascii_letters = input("Do you want to add special characters? (Y/N)")
    digits = input("Do you want to add digits?(Y/N)")
    if ascii_letters == "Y" or "y":
        characters += string.ascii_letters
    if digits == "Y" or "y":
        characters += string.digits
    break

password = [] 
for x in range(length):
   
    rchar = random.choice(characters)     
    password.append(rchar)

print("Output: " + "".join(password))