# 4.2.5_average.py
# This program reads the number untill user enter 0
# Then entered number untill 0 will be averageout and display it
# Aurthor: Akshay Pastagiya

numbers = []

number = int(input("enter number (0 to quit): "))

if number == 0 :
    numbers.append(number)

while number != 0:
    numbers.append(number)
    number = int(input("enter number (0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")