# 7_1_2_quiz2.py
# Aurthor: Akshay Pastagiya

# the with statement will automatically close the file 
#  when it is finished with it  
with open("test-b.txt", "w") as f:     
    data = f.write("test b\n") 
    # returns the number of chars written     
    print (data)  
with open("test-b.txt", "w") as f2: 
    # open file again     
    data = f2.write("another line\n")      
    print (data) 


# Question:
# 1. Look at the program below, if the file test-b.txt does not exist, 
#    what will be outputted to the console when this program is run? 
# 2. What will the contents of the file test-b.txt be when this program is run?
# 
# Answer:
# 1.  test-b.txt will be created and write down the content if data to be witeen in f.write function.
#     and oputput of the program will be number charater present in the test file
# 2.  Content of test file will be when we run 1st part of the program content will be
#     "test b" and in the 2nd part of the program content will be overwrite 
#     as we open the text file in write mode not in append mode. 
#     So, at the ene of the program the content of the file will be "another line"
