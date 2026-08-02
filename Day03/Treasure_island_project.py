print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Choose a direction (Left(L) Or Right(R))").upper()
if direction == "L":
    print("You arrive on a wall")
    print("Game over")
elif direction == "R":
    print("Moving ahead")
    print("You arrived at a lake")
    action = input("Choose action :wait(W) or swim(S)").upper()
    if action == "W":
        print("You cant find the treasure by waiting")
    elif action == "S":
        print("You crossed the lake")
        print("Moving ahead")
        print("You have almost reached choose the correct door ")
        print("Red(R),Yellow(Y),Blue(B)")
        door = input("Choose a door :").upper()
        if door == "R":
            print("You unleashed monsters on yourself")
            print("Game over")
        elif door == "Y":
            print("You fell into a wormhole")
            print("Game over")
        elif door == "B":
            print("Hooray!!! You found the treasure")
        else :
            print("Select the appropriate door only")
    else:
        print("Only two actions allowed")
else:
    print("Invalid input")










