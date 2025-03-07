# 5.1.3_queue.py
# This program is to generate the 10 randon number
# Then Place that number in to queue and then take the 1st number from the queue and remove it form queue
# Diaplay the remaining number from queue
# Aurthor: Akshay Pastagiya

import random
queue = []
numberofnumber = 10
rangeto = 100

for n in range(0,numberofnumber):
    queue.append(random.randint(0,rangeto))

print(f"queue is {queue}")

while len(queue) != 0:
    currentnumner = queue.pop(0)
    print(f"current number is {currentnumner} and the queue is {queue}")

print("The queue is now empty")
