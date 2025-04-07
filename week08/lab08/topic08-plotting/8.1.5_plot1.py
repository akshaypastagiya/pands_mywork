# 8.1.5_plot.py
# This program is to plot the graph of y=x^2
# In this program we will be using numpy to generate the randon value
# Using Matplot we will be ploting the graph
# Aurthor: Akshay Pastagiya

# import numpy and matplot library
import numpy as np
import matplotlib.pyplot as plt

# genrate random number between 1 to 100
xpoint = np.array(range(1,101))
# Generate x^2 and assign it to Y point
ypoint = xpoint * xpoint

# Create Plot
plt.plot(xpoint,ypoint,label="y = x^2")
plt.legend()
# Add a title to the plot
plt.title("Plot of y = x^2")
# Display Plot
plt.show()