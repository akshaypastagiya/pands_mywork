# 4.2.2_guess1.py
# Input the number untill user enter the correct number to guess
# Aurthor: Akshay Pastagiya

numbertoguess = 20

guess = int(input("Please guess the number: "))

while guess != numbertoguess :
    print("wrong")
    guess = int(input("Please guess again: "))

print(f"Wel done! Yes the number was {numbertoguess}")