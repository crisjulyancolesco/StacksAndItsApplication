# STACKS AND ITS APPLICATION
# Initialize the stack with capacity of & elements only
Size = 7
Stack = [0] * Size
Top = -1

# PUSH - add a new element at the top of the stack
def Push(Data):
    global Top
    if Top == Size - 1: # Checks if the size reached the capacity of the stack
        print("\n***The stack is in OVERFLOW condition.***")
    
    if Top != Size - 1: # Add the number at the top of the stack
        Top = Top + 1
        Stack[Top] = Data
        print(f"The Number {Data} is PUSHED on the stack")

# POP - removes the top element
def Pop():
    global Top
    if Top >= 0: # Remove the number at the top of the stack
        Data = Stack[Top]
        Top = Top - 1
        print(f"\nThe Number {Data} is POPPED on the stack.")
        return Data
    
    else: # Checks if the stack capacity reached 0 
        print("\n***The stack is in UNDERFLOW condition.***")

# DISPLAY - display the elements present in the stack
def Display():
    if Top == -1: # Checks if the stack is empty
        print("\n***The Stack is empty.***")

    else: # Prints all the elements in the stack
        print("\nThe contents of the stack is:  ")
        for i in Stack[:Top+1]:
            print(i)
    
# MAINMENU - Main program of the application
def MainMenu():
    global UserInput, El
    while True:
        print("")
        print("""******* CRIS STACK APPLICATION ********
*****  Cris Stack Menu            *****
*****  1. Push                    *****
*****  2. Pop                     *****
*****  3. Display Stack Contents  *****
*****  4. Exit                    *****
***************************************""")

        # Calls the operations based on the input of the user
        UserInput = int(input("Enter your choice: "))
        
        # Push operation
        if UserInput == 1:
            El = int(input("\nEnter the number to be pushed into the stack: "))
            Push(El)
        
        # Pop operation
        if UserInput == 2:
            Pop()

        # Display operation
        if UserInput == 3:
            Display()

        # Exit operation
        if UserInput == 4:
            Exit = input("\nDo you want to close CRIS STACK APPLICATION? y/n: ")
            if Exit == 'y':
                print("\nThank you for using CRIS STACK APPLICATION!")
                break
            else: 
                return MainMenu()
        
# Start the Program
MainMenu()