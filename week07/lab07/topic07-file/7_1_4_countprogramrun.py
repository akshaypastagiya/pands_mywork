# 7_1_4_countprogramrun.py
# This program is to count the number of time program run
# To do this we will store the count in test file
# Read the count add the count each time when program run
# save the count in the same file
# Aurthor: Akshay Pastagiya

# Import OS function to check file
import os.path
FILENAME = "count.txt"
# Define function to Checke file name exist or not if not exist then create one
def init():
    if not os.path.isfile(FILENAME):
        print("File doesnot exist")
        writecount(0)
    
# Define function to read number from file
def readcount():
    with open(FILENAME, 'r') as f:
        number = int(f.read())
        return number

# Define function to write nummber to the file
def writecount(number):
    with open(FILENAME, 'w') as f:
        f.write(str(number))

# call function to check file exist or not
init()
# call function to read file data
num = readcount()
num+=1
# Call function to Write value in file
writecount(num)
print(f"we have run this program {num} times")