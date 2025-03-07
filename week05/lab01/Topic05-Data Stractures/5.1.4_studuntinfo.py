# 5.1.4_studuntinfo.py
# This program is to store the studunt info like Nmae, course, grade in to dist variable
# Display the Studunt Info
# Aurthor: Akshay Pastagiya

studunt = {
    "name" : "Akshay",
    "module" : 
    [
        {
            "coursename" : "Programming",
            "grade" : 75
        },
        {
            "coursename" : "History",
            "grade" : 65
        }
    ]
}
print(f"studunt: {studunt['name']}")
for module in studunt["module"]:
    print(f"\t {module['coursename']} : {module['grade']}")