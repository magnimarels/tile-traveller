# Fyrst ætlum við að búa til fall sem tekur inn bool: boolN, boolS, boolW og boolE.
# Svo búum við if statemetn fyrir hvert tile. Það gefur svo út hvað á að prenta
# 
player_location = "1, 1"

def what_direction(N, E, S, W):
    output = ""
    if N == True:
        output = output + "(N)orth "
    if E == True:
        output = output + "(E)ast"
    if S == True:
        output = output + "(S)outh"
    if W == True:
        output = output + "(W)est"

if player_location == "1, 1":
    to_be_printed = what_direction(True, False, False, False)
    print("You can travel: {} or {}.".format(to_be_printed))
    player_input = input("Direction: ").capitalize()
    if player_input == "N":
        player_location = "1, 2"
    else:
        print("Not a valid direction!")
        print("You can travel: {} or {}.".format(to_be_printed))
if player_location == "1, 2":
    to_be_printed = what_direction(True, True, True, False)
    print("You can travel: {} or {} or {}.".format(to_be_printed))
    player_input = input("Direction: ").capitalize()
    if player_input == "N":
        player_location = "1, 2"
    elif player_input == "S":
        player_location = "2, 2"
    elif player_input == "W":
        player_location = "1, 3"
    else:
        print("Not a valid direction!")
        print("You can travel: {} or {} or {}.".format(to_be_printed))
if player_location == "1, 3":
    to_be_printed = what_direction(False, True, True, False)
    print("You can travel: {} or {}.".format(to_be_printed))
    player_input = input("Direction: ").capitalize()
    if player_input == "E":
        player_location = "2,3"
    elif player_input == "S":
        player_location = "1, 2"
    else:
        print("Not a valid direction!")
        print("You can travel: {} or {}.".format(to_be_printed))
        








          