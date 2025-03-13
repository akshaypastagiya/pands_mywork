# This is the 6_1_2_displaymenu.py
# This program is to create a function 
# This function is to view the studunt menu
# Menu is like Add or View the studunt or quit the function
# Aurthor: Akshay Pastagiya

def displaymenu():
    print("What would you like to do?")
    print("\t (a) Add new Student")
    print("\t (v) View Students")
    print("\t (q) Quit")
    choice = input("Type one letter (a/v/q): ")
    # Return the selected charater
    return choice

# Display your selected return charater from function
print(f"you chose {displaymenu()}")