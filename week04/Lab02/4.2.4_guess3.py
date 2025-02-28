# 4.2.4_guess3.py
# will generate the rendom number between 1 to 100
# user will Input the number untill user enter the correct number to guess
# User will get the hint if enter number is too high or too low
# Aurthor: Akshay Pastagiya

import random

numbertoguess = random.randrange(1,100)

guess = int(input("Please guess the number: "))

while guess != numbertoguess :
    if guess < numbertoguess :
        print("too low") 
    else:
        print("too high") 

    guess = int(input("Please guess again: "))

print(f"Wel done! Yes the number was {numbertoguess}")