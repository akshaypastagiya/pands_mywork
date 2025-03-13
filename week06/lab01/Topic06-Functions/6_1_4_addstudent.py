# This is the 6_1_4_addstudent.py
# This program is to create a function 
# This function is to view the studunt menu
# Menu is like Add or View the studunt or quit the function
# When say a it will call for add function this function will add studunt name.
# when say v it will call for view function
# when say q it will call fror quit function
# Aurthor: Akshay Pastagiya


# Create display menu function
def displaymenu():
    print("What would you like to do?")
    print("\t (a) Add new Student")
    print("\t (v) View Students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q): ")
    # Return the selected charater
    return choice
# Create Studunts as dist
students = []

def readmodules():
    return[]

# Create add studunt function
def doadd(students):
    # Create Current student as dist
    currentstudent = { }
    # Get Student Name
    currentstudent["name"] = input("Enter Student name: ")
    # Get Module Information
    currentstudent["modules"] = readmodules()

    # Add Studunt Information and module information
    students.append(currentstudent)
    

# Create View Function
def doview():
    print("Viewing")

selectedchoice = displaymenu()

while (selectedchoice != 'q'):
    #call for add function if selected charater as a
    if selectedchoice == 'a':
        doadd(students)
    elif selectedchoice == 'v':
        doview()
    elif selectedchoice == 'q':
        # Display your selected return charater from function
        print(f"you chose {selectedchoice}")
    else:
        print("\n\n Please select either a, v or q:")
    
    
    selectedchoice = displaymenu()
print(students)
