x = 'y' 
while (x == 'y' or x == 'Y'):

    first_input = int(input("enter the number: "))
    print("Select operator + - * /")
    operator_input = input("Enter here: ")
    second_input = int(input("enter the number: "))

    def add():

        final_output = first_input+second_input
        print("Addition of " ,first_input, "and" ,second_input, "is", final_output)

    def subtraction():
        final_output = first_input-second_input
        print("Subtraction  of " ,first_input, "and" ,second_input, "is", final_output)

    def multiple():
        final_output = first_input*second_input
        print("Multiply of " ,first_input, "and" ,second_input, "is", final_output)
    
    def division():
        final_output = first_input/second_input
        print("Division  of " ,first_input, "and" ,second_input, "is", final_output)
        

    if operator_input == '+':
        add()
    elif operator_input == '-':
        subtraction()
    elif operator_input == '*':
        multiple()
    elif operator_input == '/':
        division()
    else:
        print("Enter the valid operator ")

    x = input("you want to continue y/n: ")

    if x == 'n' or x == 'N':
        print("Thanks for using")
        break

else: 
    print("Enter valid input ")
        
