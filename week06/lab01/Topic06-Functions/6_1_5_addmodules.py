# This is the 6_1_5_addmodule.py
# This program is to create a function 
# This function is to view the studunt menu
# Menu is like Add or View the studunt or quit the function
# When say a it will call for add function this function will add studunt name, modulename and grade of the studunt untill we enter blank as module name
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

students = []

#Create Module function
def readmodules():
    # Define Modules
    modules = []
    # Get Module name
    modulename = input("\t Enter the first module name (blank to quit): ")
    # Check module name is blank or not
    while modulename != "":
        # Define Module
        module = {}
        module["name"] = modulename
        # Get Grade of the module
        module["grade"] = int(input("\t Enter grade: "))
        # Appent Module Name and respactive Grade togather
        modules.append(module)
        # Get net module name if blank then return
        modulename = input("\t Enter the next module name (blank to quit): ")
    return modules

# Create add student function
def doadd(students):
    # defune Current student as dist
    currentstudent = { }
    # Get current Student Name
    currentstudent["name"] = input("Enter Student name: ")
    # Get Module Information by calling readmodule function
    currentstudent["modules"] = readmodules()

    # Append Studunt Information and relative module information
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
