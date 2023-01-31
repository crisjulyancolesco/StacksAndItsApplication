# STACKS AND ITS APPLICATION
Size = 7
Stack = [0] * Size
Top = -1

# PUSH - add a new element into the stack
def Push(Data):
    global Top
    if Top == Size - 1:
        print("The stack is in overflow condition.")
    
    if Top != Size - 1:
        Top = Top + 1
        Stack[Top] = Data
        print(f"The Number {Data} is pushed on the stack")

def Pop():
    global Top
    if Top > 0:
        Data = Stack[Top]
        Top = Top - 1
        print(f"The Number {Data} is popped on the stack.")
        return Data
    else:
        print("The stack is in underflow condition.")

def Display():
    if Top == -1:
        print("The Stack is empty.")

    else:
        print("The contents of the stack is:  ")
        for i in Stack[:Top+1]:
            print(i)
    

def MainMenu():
    global UserInput, El
    while True:
        print("")
        print("""***************************************
*****  My Stack Menu              *****
*****  1. Push                    *****
*****  2. Pop                     *****
*****  3. Display Stack Contents  *****
*****  4. Exit                    *****
***************************************""")

        UserInput = int(input("Enter your choice: "))
        
        if UserInput == 1:
            El = int(input("Enter the number to be pushed into the stack: "))
            Push(El)
        
        if UserInput == 2:
            Pop()

        if UserInput == 3:
            Display()

        if UserInput == 4:
            Exit = input("Do you want to close STACK APPLICATION? y/n: ")
            if Exit == 'y':
                print("\nThank you for using STACK APPLICATION!")
                break
            else: 
                return MainMenu()
        
# Start the Program
MainMenu()