# 8.1.11_piechart.py
# create arrey of county
# generate 100 randon to pick from the counties list created
# Plot the pie chart for the counties number of times apper in the list
# Aurthor: Akshay Pastagiya

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possibleCounties = ['mayo', 'Galway', 'Limerick', 'Clare', 'Rosommon', 'Dublin','Donegal']

# pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice(possibleCounties ,p=[0.1, 0.13, 0.17, 0.22, 0.07, 0.15, 0.16 ],size=(100))

# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)

# we can now put this into a pie plot
plt.bar(unique, counts)
plt.show()
