# salaries1.py
# generate 10 randon numbers between 20000 - 80000 using numpy
# add 5000 bonus in to the salary
# Aurthor: Akshay Pastagiya

# import numpy library
import numpy as np

# assign minimum and maximum salary
minsalary = 20000
maxsalary = 80000

# assign number of random salary needs to generate
numberofentries  = 10

# Generate randon number using numpy
salaries = np.random.randint(minsalary,maxsalary,numberofentries)
# add 5000 to the random number
salariesplus = salaries + 5000
print(salaries)
print(salariesplus)