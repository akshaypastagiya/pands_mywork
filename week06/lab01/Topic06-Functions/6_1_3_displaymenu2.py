# This is the 6_1_3_displaymenu2.py
# This program is to create a function 
# This function is to view the studunt menu
# Menu is like Add or View the studunt or quit the function
# When say a it will call for add function
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

# Create add function
def doadd():
    print("adding")

# Create View Function
def doview():
    print("Viewing")

selectedchoice = displaymenu()

while (selectedchoice != 'q'):
    #call for add function if selected charater as a
    if selectedchoice == 'a':
        doadd()
    elif selectedchoice == 'v':
        doview()
    elif selectedchoice == 'q':
        # Display your selected return charater from function
        print(f"you chose {selectedchoice}")
    else:
        print("\n\n Please select either a, v or q:")
    
    selectedchoice = displaymenu()