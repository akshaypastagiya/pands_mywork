# 3.1.4_randomgenerator.py
# This program is to generate random number
# Display generated random number
#Aurthor: Akshay Pastagiya

import random

x = int(input("Enter minimum number : "))
y = int(input("Enter maximum number : "))

number = random.randint(x,y)

print(f"Here is random generated between {x} and {y} is {number}")