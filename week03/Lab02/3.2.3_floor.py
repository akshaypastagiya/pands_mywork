# 3.2.3_floor.py
# This program use a library called math
# Using math library convert float value in to integer valuse but integer valuse will be rounded down
# Aurthor: Akshay Pastagiya

import math

number = float(input("Enter a float number: "))

floorednumber  = math.floor(number)

print("{} floored is {}".format(number,floorednumber))