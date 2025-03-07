# 5.1.5_studentinfo.py
# This program is to store the studunt info like Nmae, course, grade in to dist variable
# Store Studunt name untill studunt name is blank
# and add student info untill the studunt course name as blank
# Display the Student Info
# Aurthor: Akshay Pastagiya

students = []

newname = input("Enter the studunt name if you want to add (or press enter to finish) ")

while newname != "":

    student = {"name":newname,"module":[]}   
               
    newcoursename = input("Enter Course name if you want to add (or press enter to finish) ")

    while newcoursename != "":
        newgrade = input(f"Enter the grade for {newcoursename} ")
        student["module"].append({"coursename":newcoursename,"grade": newgrade})
        newcoursename = input("Enter Course name if you want to add (or press enter to finish)")
        if newcoursename == "":
            break
    students.append(student)
    newname = input("Enter the studunt name if you want to add (or press enter to finish) ")
    if newname == "":
        break


for student in students:
    print(f"student: {student["name"]}")
    for modules in student["module"]:
        print(f"\t {modules["coursename"]} : {modules["grade"]}")