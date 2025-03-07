# 5.1.1_question.py
# This Program is to reply the answer of the question ask in Lab05
# Questions are commented in program
# Question are to disply the types of variable assign in the program
# Author: Akshay Pastagiya

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")
me = {
    "firstName" : "Andrew",
    "teaching" : 
    [
        {
        "courseName" : "programming",
        "semester" : 1
        },
        {
        "courseName" : "Data Representation",
        "semester" : 2
        }
    ]
}

'''
    What are the variable types of the following variables in the code above
        a. numberOfQuestions
        b. averageAge
        c. debugMode
        d. name
        e. ages
        f. months
        g. months[1]
        h. book
        i. stuff
        j. stuff[2]
        k. someone
        l. someone["firstname"]
        m. me
        n. me["teaching"]
        o. me["teaching"][0]["semester"]
        p. me["teaching"][0]["coursename"]
'''
print(f"variable type of numberOfQuestions is {type(numberOfQuestions)}")
print(f"variable type of averageAge is {type(averageAge)}")
print(f"variable type of debugMode is {type(debugMode)}")
print(f"variable type of name is {type(name)}")
print(f"variable type of ages is {type(ages)}")
print(f"variable type of months is {type(months)}")
print(f"variable type of months[1] is {type(months[1])}")
print(f"variable type of book is {type(book)}")
print(f"variable type of stuff is {type(stuff)}")
print(f"variable type of stuff[2] is {type(stuff[2])}")
print(f"variable type of someone is {type(someone)}")
print(f"variable type of someone[firstname] is {type(someone['firstname'])}")
print(f"variable type of me is {type(me)}")
print(f"variable type of me[teaching] is {type(me['teaching'])}")
print(f"variable type of me[teaching][0][semester] is {type(me['teaching'][0]['semester'])}")
print(f"variable type of me[teaching][0][courseName] is {type(me['teaching'][0]['courseName'])}")