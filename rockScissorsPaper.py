import time
import random

def getFromPlayer():
    valid_input = False
    while not valid_input:
        try:
            picked = int(print("OK! pick one between 'em:\n\t1. Rock\n\t2. Scissors\n\t3. Paper\n\n\t"))
            valid_input = True
        except ValueError:
            print("Invalid input. Try again")
        except:
            print("Unknown error")
    return picked

def getElement(value_picked):
    if (value_picked == 1):
        return "Rock"
    elif(value_picked == 2):
        return "Scissors"
    elif(value_picked == 3):
        return "Papaer"
    else:
        print("A BRUTAL ERROR OCCURRED")
        return "ERROR"

def getFromPC():
    return random.randint(1, 3)

def primary():
    print("Starting the game Rock Scissors Paper...")
    time.sleep(1)   #PY will sleep for 1 sec





primary()