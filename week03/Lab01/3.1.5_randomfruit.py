# 3.1.5_randomfruit.py
# This program prints out a random fruit
# Aurthor: Akshay Pastagiya


import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(f"A Random Fruit: {fruit}")