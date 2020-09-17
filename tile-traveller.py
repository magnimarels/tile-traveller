
player_location = "1, 1"


while player_location != "3, 1":
    if player_location == "1, 1":

        print("You can travel: (N)orth.")
        player_input = input("Direction: ").capitalize()
        if player_input == "N":
            player_location = "1, 2"
        else:
            print("Not a valid direction!")
    if player_location == "1, 2":

        print("You can travel: (N)orth or (E)ast or (S)outh.")
        player_input = input("Direction: ").capitalize()
        if player_input == "N":
            player_location = "1, 3"
        elif player_input == "S":
            player_location = "1, 1"
        elif player_input == "E":
            player_location = "2, 2"
        else:
            print("Not a valid direction!")
    if player_location == "1, 3":

        print("You can travel: (E)ast or (S)outh.")
        player_input = input("Direction: ").capitalize()
        if player_input == "E":
            player_location = "2, 3"
        elif player_input == "S":
            player_location = "1, 2"
        else:
            print("Not a valid direction!")
    if player_location == "2, 1":

        print("You can travel: (N)orth.")
        player_input = input("Direction: ").capitalize()
        if player_input == "N":
            player_location = "2, 2"
        else:
            print("Not a valid direction!")

    if player_location == "2, 2":

        print("You can travel: (S)outh or (W)est.")
        player_input = input("Direction: ").capitalize()
        if player_input == "S":
            player_location = "2, 1"
        elif player_input == "W":
            player_location = "1, 2"
        else:
            print("Not a valid direction!")

    if player_location == "2, 3":

        print("You can travel: (E)ast or (W)est.")
        player_input = input("Direction: ").capitalize()
        if player_input == "E":
            player_location = "3, 3"
        elif player_input == "W":
            player_location == "1, 3"
        else:
            print("Not a valid direction!")

    if player_location == "3, 3":

        print("You can travel: (S)outh or (W)est.")
        player_input = input("Direction: ").capitalize()
        if player_input == "W":
            player_location = "2, 3"
        elif player_input == "S":
            player_location = "3, 2"
        else:
            print("Not a valid direction!")

    if player_location == "3, 2":

        print("You can travel: (N)orth or (S)outh.")
        player_input = input("Direction: ").capitalize()
        if player_input == "N":
            player_location = "3, 3"
        elif player_input == "S":
            player_location = "3, 1"
        else:
            print("Not a valid direction!")
else: 
    print("Victory!")