# Fyrst ætlum við að búa til fall sem tekur inn bool: boolN, boolS, boolW og boolE.
# Svo búum við if statemetn fyrir hvert tile. Það gefur svo út hvað á að prenta
# 
player_location = "1, 1"

def what_direction(N, S, E, W):
    output = ""
    if N == True:
        output = output + "(N)orth "
    if S == True:
        output = output + "(S)outh"
    if E == True:
        output = output + "(E)ast"
    if W == True:
        output = output + "(W)est"


if player_location == "1, 1":
    to_be_printed = what_direction(True, False, False, False)
    print("You can travel: ", to_be_printed, "." )
    player_input = input("Direction: ").capitalize()
    if player_input == "N":
        player_location = "1, 2"
    else:
        print("Not a valid direction!")
        player_input = input("Direction: ")
if player_location == "1, 2":
    to_be_printed = what_direction(True, False, False, False)
    print("You can travel: ", to_be_printed, "." )
    player_input = input("Direction: ").capitalize()
    if player_input == "N":
        player_location = "1, 2"
    else:
        print("Not a valid direction!")
        player_input = input("Direction: ").capitalize()








          