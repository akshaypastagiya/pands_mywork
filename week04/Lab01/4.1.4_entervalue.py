# 4.1.4_entervalue.py
# This program is to prompting to enter value untill user enter value as -1
# Aurthor: Akshay Pastagiya

number = int(input("Enter the number: "))

while number != 1:
    print("Number is not minus one")
    number = int(input("Enter the number: "))
    if number == -1:
        print("Number is minus one")
        break