# salaries1.py
# generate 10 randon numbers between 20000 - 80000 using numpy
# add salary increment as 1.5%
# save incremented salary in to another array
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
# aincrement salary by 5%
salaryincrement = int(salaries + (salaries*0.05))
# convery incremented salary value in to int
newsalaries = salaryincrement.astype(int)

print(salaries)
print(newsalaries)