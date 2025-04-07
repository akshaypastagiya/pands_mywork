# 8.1.8_2plot.py
# generate 100 randon numbers between 20000 - 80000 using numpy
# generate 100 randon numbers between 21 - 65 as age using numpy
# This program is to plot the graph of y=x^2
# Create Scatter plot of the age and and salary
# create plot graph of y=x^2
# Display both graph
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

# genrate random number between 1 to 100
xpoint = np.array(range(1,101))
# Generate x^2 and assign it to Y point
ypoint = xpoint * xpoint

# Create the Scatter plot of the salary vs age
plt.scatter(salaries,age,label = "Salry vs age")
# Add title and labels
plt.title("Salary vs age Distribution")

# Create y=x^2 Plot
plt.plot(xpoint,ypoint,label="y = x^2", color = 'r')
# Add a title to the plot
plt.title("Salary vs age Distribution \n and Plot of y = x^2")
plt.legend()
# Display Plot
plt.show()