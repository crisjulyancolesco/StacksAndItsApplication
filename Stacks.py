# STACKS AND ITS APPLICATION

def MainMenu():
    global UserInput
    print("")
    print("""***************************************
*****  My Stack Menu              *****
*****  1. Push                    *****
*****  2. Pop                     *****
*****  3. Display Stack Contents  *****
*****  4. Exit                    *****
***************************************""")

    UserInput = int(input("Enter your choice: "))

    while True:
        if UserInput == 1:
            Push()
        
        if UserInput == 2:
            Pop()

        if UserInput == 3:
            Display()

        if UserInput == 4:
            break
        
        else:
            print("Invalid Input!")
            return MainMenu()

# Start the Program
MainMenu()