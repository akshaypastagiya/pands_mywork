# 8.1.7_scatterplot.py
# generate 100 randon numbers between 20000 - 80000 using numpy
# generate 100 randon numbers between 21 - 65 as age using numpy
# Create Scatter plot of the age and and salary and display the plot
# Aurthor: Akshay Pastagiya

# import numpy and matplot library
import numpy as np
import matplotlib.pyplot as plt


# assign minimum and maximum salary
minsalary = 20000
maxsalary = 80000
minage = 21
maxage = 65

# assign number of random salary needs to generate
numberofentries  = 100
#generate same random values
np.random.seed(1)

# Generate randon number using numpy
salaries = np.random.randint(minsalary,maxsalary,numberofentries)
age = np.random.randint(minage,maxage,numberofentries)

# Create the Scatter plot of the salary vs age
plt.scatter(salaries,age,label = "Salry vs age")
# Add title and labels
plt.title("Salary vs age Distribution")
plt.xlabel("Salary")
plt.ylabel("age")
plt.legend()

# Display Plot
plt.show()