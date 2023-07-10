print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

dir=input("You are at a cross road. which direction do you want to go? enter 'left' or 'right'\n")
if dir =='left':
    act=input("You arrive at a lake, and island is middle of the lake. You can 'wait' for the boat or 'swim' across the lake. make your choice? 'wait' or 'swim'?\n")
    if act =='wait':
        door = input("You arrived on the island unharmed, and see house with three doors with 'red', 'blue' and 'yellow' colored. which door you want to open? 'red', 'blue' or 'yellow'? \n")
        if door =='red':
            print("You were Burned by fire!\n GAME OVER!!")
        elif door =='blue':
            print("You were eaten by beasts!\n GAME OVER!!")
        elif door =='yellow':
            print("you found the Treasure!\n WINNER!!")
        else:
            print("GAME OVER!!")
    else:
        print("You were attacked by trout!\n GAME OVER!!")


else:
    print("you fell into a hole! \n GAME OVER!!")


