# 3.1.3div.py
# This program is to division of the 2 number
# Input Number 1 and Number 2
# Display answer Number 1 divide by number 2

number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))

answer = int(number1/number2)
reminder = number1%number2

print(f"{number1} divid by {number2} is {answer} with reminder {reminder}")