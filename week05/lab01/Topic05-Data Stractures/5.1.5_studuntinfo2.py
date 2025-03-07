# 5.1.5_studuntinfo.py
# This program is to store the studunt info like Nmae, course, grade in to dist variable
# Store the studunt infor untill the studunt course name as blank
# Display the Studunt Info
# Aurthor: Akshay Pastagiya

studunt = {
    "name" : "Akshay",
    "module" : 
    [
        {
            "coursename" : "Programming",
            "grade" : 45
        },
    ]
}

newcoursename = input("Enter Course name if you want to add (or press enter to finish) ")

while newcoursename != "":
    newgrade = input(f"Enter the grade for {newcoursename} ")
    studunt["module"].append({"coursename":newcoursename,"grade": newgrade})
    newcoursename = input("Enter Course name if you want to add (or press enter to finish)")
    if newcoursename == "":
        break

print(f"studunt: {studunt['name']}")

for module in studunt["module"]:
    print(f"\t {module['coursename']} : {module['grade']}")