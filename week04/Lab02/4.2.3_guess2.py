# 4.2.3_guess2.py
# Input the number untill user enter the correct number to guess
# User will get the hint if enter number is too high or too low
# Aurthor: Akshay Pastagiya

numbertoguess = 20

guess = int(input("Please guess the number: "))

while guess != numbertoguess :
    if guess < numbertoguess :
        print("too low") 
    else:
        print("too high") 

    guess = int(input("Please guess again: "))

print(f"Wel done! Yes the number was {numbertoguess}")