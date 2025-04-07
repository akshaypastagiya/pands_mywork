# 8.1.6_HistPlot.py
# generate 10 randon numbers between 20000 - 80000 using numpy
# Create Histogram of the salary and display
# Aurthor: Akshay Pastagiya

# import numpy and matplot library
import numpy as np
import matplotlib.pyplot as plt


# assign minimum and maximum salary
minsalary = 20000
maxsalary = 80000

# assign number of random salary needs to generate
numberofentries  = 10

# Generate randon number using numpy
salaries = np.random.randint(minsalary,maxsalary,numberofentries)

# Create the Histogram of the salary
plt.hist(salaries, label = "Salary vs frequency")
# Add title and labels
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.legend()
# Display Plot
plt.show()