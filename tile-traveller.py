# Fyrst ætlum við að búa til fall sem tekur inn bool: boolN, boolS, boolW og boolE.
# Svo búum við if statemetn fyrir hvert tile. Það gefur svo út hvað á að prenta
# 
player_location = "1, 1"

def what_direction(N, S, A, W):
    output = ""
    if N == True:
        output = output +   "North "


if player_location == "1, 1":
    to_be_printed = what_direction(True, False, False, False)
    print("You can travel: ", to_be_printed, "." )
    player_input = input("Direction: ")
    if player_location






          