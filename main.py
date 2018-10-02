def add(num1, num2):
    """Returns num1 plus num2. One stop programming is cool"""
    return num1 + num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Handled div by zero. Returning zero")
        return 0


"""def switch_ope(operation, num1, num2):
    return {
    'add' : add(num1,num2),
    'subtract' : sub(num1,num2),
    'sub' : sub(num1,num2),
    'multiply' : mul(num1,num2),
    'mul' : mul(num1,num2),
    'mult' : mul(num1,num2),
    'divide' : div(num1,num2),
    'div' : div(num1,num2)
}[operation]"""                    #Without this '[operation]' tutti i valori verrebbero printati

def main():
    for i in range(3):
    #user_continue = True
    #while user_continue:
        valid_input = False
        while not valid_input:
            # Get User Input
            try:
                num1 = int(input("Give me number 1  "))
                num2 = int(input("Give me number 2  "))
                operation = int(input("What do you want to do?\n\t1. add,\n\t2. subtract,\n\t3. multiply,\n\t4. divide"
                                      "\nEnter a number"))
                valid_input = True
            except ValueError:
                print("Invalid input. Try again")
                # return # Exit program 'cause of an error #not needed anymore perché richiede l'input all'utente
            except:
                print("Unknown error")
        # Determine operation
        if(operation==1):
            print("Adding...")
            print(add(num1, num2))
        elif(operation==2):
            print("Subtracting...")
            print(sub(num1, num2))
        elif(operation==3):
            print("Multiplying...")
            print(mul(num1, num2))
        elif(operation==4):
            print("Dividing...")
            print(div(num1, num2))
        else:
            print("Input incorrect")
        # Ask uer to continue
            """user_yn = input("Would you like to run another calculation? Type 'y' for yes, other any value to exit")
            if (user_yn!= 'y'):
                user_continue = False
                break
            else:
             continue"""

    #print(switch_ope(operation, num1, num2))
    """The switch_ope is used in order to avoid multiple if-elif-elif-elif-else statement"""
    #print(add(num1,num2))
    #print(sub(num1,num2))
    #print(mul(num1,num2))
    #print(div(num1,num2))


main()