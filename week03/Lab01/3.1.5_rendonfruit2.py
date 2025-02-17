# 3.1.5_randomfruit2.py
# This program prints out a random fruit
# This program is to showcase the functinality of Truple
# Aurthor: Akshay Pastagiya


import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print(f"A Random Fruit: {fruit}")