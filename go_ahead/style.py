import random
computer = random.choice(["snake","gun","water"])

# print(computer)

player = input("enter your choice: ")


if computer == player :
    print("***DRAW***")


elif computer == "snake"and player == "water" :
    print("***COMPUTER WON THE GAME***")


elif computer == "water" and player == "snake" :
    print("***PLAYER WON THE GAME***")


elif computer == "gun" and player == "snake" :
    print("***COMPUTER WON THE GAME***")


elif computer == "snake" and player == "gun" : 
    print("***PLAYER WON THE GAME***")


elif computer == "water" and player == "gun" :
    print("***COMPUTER WON THE GAME***")


elif computer == "gun" and player == "water" : 
    print("***PLAYER WON THE GAME***")
else :
    print("INVALID INPUT,SOME THING WENT WRONG!!!")