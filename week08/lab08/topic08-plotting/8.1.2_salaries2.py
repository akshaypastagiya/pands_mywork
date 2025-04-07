# salaries2.py
# generate 10 randon numbers between 20000 - 80000 using numpy
# each time when we generate randon number it will be same everytime
# Aurthor: Akshay Pastagiya

# import numpy library
import numpy as np

# assign minimum and maximum salary
minsalary = 20000
maxsalary = 80000

# assign number of random salary needs to generate
numberofentries  = 10

# Aks Numpy to generate same random value
np.random.seed(1)
# Generate randon number using numpy
salaries = np.random.randint(minsalary,maxsalary,numberofentries)
print(salaries)