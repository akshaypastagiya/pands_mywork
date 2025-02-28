# 4.2.6_topthree.py
# This program is to generate 10 random number and Display them
# Out of that 10 which are the top three display them
# Aurthor: Akshay Pastagiya

import random

numbers = []

for i in range(1,10) :
    numbers.append(random.randint(0,100))
    
print(f"10 random numbers are {numbers}")

numbers.sort(reverse=True)

print(f"The top 3 numbers are {numbers[0:3]}")