# Infix To PostFix
Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # Operators 

Precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} # Precedence of the Operators (which operation should be processed first)
 
 # Main operator of the program (to convert infix to postfix)
def InfixToPostfix(Infix): 

    # Initialized the list(Stack)
    Stack = [] 
    Output = "" 

    # Checks every characters of the inputted infix expression 
    for Character in Infix:

        if Character not in Operators: # If character is not present in the operators, append in the output
            Output += Character

        elif Character == '(':  # If "(" present, append to the stack
            Stack.append('(')

        elif Character == ')': # If ")" is present, and if it satisfy the condition it will: 
            while Stack and Stack[-1] != '(': # Pop it from the stack the character(based on the condition at this while loop) and Append  to the output 
                Output += Stack.pop()
            Stack.pop() # then Pop the "(" from the stack

        else: # If character present in the operators except "(" or ")"
            while Stack and Stack[-1] != '(' and Precedence[Character] <= Precedence[Stack[-1]]: # Pop it from the stack and append it to the output
                Output += Stack.pop()

            Stack.append(Character)

    while Stack: # If there is only one character, it will pop the character at the stack and append it to the output
        Output += Stack.pop()
    return Output # Return the Output 


# Program driver
print("")
print("\t********** INFIX TO POSTFIX **********\t")
Infix = input("\nEnter the Infix Expression :: ")
print(f"Postfix Expression is :: {InfixToPostfix(Infix)}\n")