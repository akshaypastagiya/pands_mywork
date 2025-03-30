# 7_1_5_jsonfile.py
# This program is to understand about the Json file
# Understand how data store in json file formet similler like dist
# Aurthor: Akshay Pastagiya

import json 
FILENAME="testdict.json" 
sample= dict(name='fred', age=31, grades=[1,34,55]) 
def writeDict(obj): 
    with open(FILENAME, 'wt') as f: 
        json.dump(obj,f) 
# test the function writeDict(sample)
writeDict(sample) 

def readDict():     
    # this will throw an error if the file does not exist     
    # # it should readly just return an empty dict      
    # # we can do this later     
    with open(FILENAME) as f:         
        return json.load(f)  

# test the function 
somedict = readDict() 
print(somedict) 