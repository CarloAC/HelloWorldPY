import time
import random

def getFromPlayer():
    valid_input = False
    while not valid_input:
        try:
            picked = int(input("OK! pick one between 'em:\n\t1. Rock\n\t2. Scissors\n\t3. Paper\n\n\t"))
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

def getWinner():
    player_value = getFromPlayer()
    pc_value = getFromPC()
    tmp_value = player_value - pc_value;
    printPlayer(player_value)
    printPC(pc_value)
    if(tmp_value == 0):
        return "DRAW"
    elif((tmp_value == -1) or (tmp_value == 2)):
        return "PLAYER WINs"
    elif((tmp_value == 1) or (tmp_value == -2)):
        return "PC WINs"
    else:
        return "HOW THE HELL DO YOU GET THERE???"

def printPlayer(value):
    print("[Player]: ")
    print(getElement(value))

def printPC(value):
    print("[PC]: ")
    print(getElement(value))


def primary():
    print("Starting the game Rock Scissors Paper...")
    time.sleep(1)   #PY will sleep for 1 sec
    print(getWinner())



primary()