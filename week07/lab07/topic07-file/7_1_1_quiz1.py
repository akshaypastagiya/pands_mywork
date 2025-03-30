# 7_1_1_quiz1.py
# Aurthor: Akshay Pastagiya
  
# the with statement will automatically close the file 
# when it is finished with it 
  
with open("test-a.txt") as f: 
    data = f.read() 
    print (data) 

# the old way of doing this is  
# f = open ("test1.txt") 
#  data = f.read() 
#  print(data) 
#  f.close() 


# Question:
# Look at the program below, 
# if the file test-a.txt does not exist. 
# What will happen when the program runs? 
# Answer:
# As file test-a.txt does not exist so, program won't be able to open that file.
# Program throw an error that filenotfound

