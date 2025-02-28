# 4.1.2_graderound.py
# This Program is to check the grade of the student
# Enter Studunt percentage
# Baced of percentage entered corresponding grade will be print
# Aurthor: Akshay Pastagiya

import math

percentage = float(input("Enter the percentage: "))

percentageround = math.floor(percentage)

if percentageround < 0 or percentageround > 100:
    print("Please enter a number between 0 and 100")
elif percentageround < 40:
    print("Fail")
elif percentageround < 50:
    print("Pass")
elif percentageround < 60:
    print("Merit 2")
elif percentageround < 70:
    print("Merit 1")
else:
    print("Distinction")