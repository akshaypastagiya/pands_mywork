# 4.1.2_grade.py
# This Program is to check the grade of the student
# Enter Studunt percentage
# Baced of percentage entered corresponding grade will be print
# Aurthor: Akshay Pastagiya

percentage = float(input("Enter the percentage: "))

# percentage = round(percentage)

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else:
    print("Distinction")