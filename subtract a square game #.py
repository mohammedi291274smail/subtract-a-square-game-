# file: CS112_A1_T2_2_20231135
"""
purpose : Number scrabble is played with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw
"""
# Author: Mohamed Ismail Mohamed
# ID : 20231135
# Date : 20 feb 2024

def game():
    # Display a welcome message for the Scrabble game
    print("***** Welcome In scrabble Game *****\n")
    # Initialize variables for player scores and selected numbers

    counter = 0
    sum_1 = 0
    sum_2 = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    w = 0
    x = 0
    y = 0
    z = 0
    # Main game loop, runs for 9 turns

    while counter < 9:
        # Define a function to get integer input from player one

        def get_integer_input():
            while True:
                try:
                    player_one = int(input("Player One : Please enter number from 1 to 9\n"))
                    # Try converting the input to an integer
                    integer_value = int(player_one)
                    # If successful, break out of the loop and return the integer value
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            return integer_value
        # Call the function to get input from player one
        user_integer = get_integer_input()

        while True:
            # Validate that the entered number is in the valid range

            if user_integer not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                user_integer = int(input("player One : please inter valid number from 1 to 9 \n"))
                continue
            break
        # Check the current turn and update the selected numbers accordingly
        if counter == 0:
            a = user_integer
            print(" Now you have :  ", a, " \n")


        elif counter == 1:

            w = user_integer_2

        elif counter == 2:

            while True:
                b = user_integer
                print(" Now you have :  ", a, "and ", b, " \n")

                if counter == 2 and user_integer == a or user_integer == w:
                    if user_integer in [a, w]:
                        user_integer = int(
                            input("Player_one : Please select number that has not been selected before \n"))
                        continue
                break

        elif counter == 3:
            x = user_integer_2

        elif counter == 4:
            while True:
                c = user_integer
                print(" Now you have :  ", a, ",", b, "and", c, " \n")

                if counter == 4 and user_integer == a or user_integer == w or user_integer == b or user_integer == x:
                    if user_integer in [a, w, b, x]:
                        user_integer = int(
                            input(" player_one : Please select number that has not been selected before \n"))
                        continue
                break

        elif counter == 5:
            y = user_integer_2


        elif counter == 6:

            while True:
                d = user_integer
                print(" Now you have :  ", a, ", ", b, ",", c, " and ", d, " \n")


                if counter == 6 and user_integer == a or user_integer == w or user_integer == b or user_integer == x or user_integer == c or user_integer == y:

                    if user_integer in [a, w, b, x, c, y]:
                        user_integer = int(
                            input(" player_one :  please select number that has not been selected before \n"))
                        continue
                break

        elif counter == 7:
            z = user_integer_2

        elif counter == 8:

            while True:
                e = user_integer
                print(" Now you have :  ", a, ", ", b, ",", c, " , ", d, " and", e, " \n")

                if counter == 8 and user_integer == a or user_integer == w or user_integer == b or user_integer == x or user_integer == c or user_integer == y or user_integer == d or user_integer == z:

                    if user_integer in [a, w, b, x, c, y, d, z]:
                        user_integer = int(
                            input("player_one : Please select number that has not been selected before \n"))
                        continue
                break

        #sum_1 = sum_1 + player_one
        counter = counter + 1
        if counter == 9:
            break

        #player_two = int(input("Player Two : Please enter a number from 1 to 9\n"))
        def get_integer_input_2():
            while True:
                try:
                    #user_input = input("Enter an integer: ")
                    player_two = int(input("Player two : Please enter number from 1 to 9\n"))
                    # Try converting the input to an integer
                    integer_value_2 = int(player_two)
                    # If successful, break out of the loop and return the integer value
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            return integer_value_2

        # Example usage:
        user_integer_2 = get_integer_input_2()
        while True:

            if user_integer_2 not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                user_integer_2 = int(input("player two : please inter valid number from 1 to 9 \n"))
                continue
            break
        if counter == 1:

            while True:
                w = user_integer_2
                print(" Now you have : ", w, "\n")

                if counter == 1 and user_integer_2 == a:

                    if user_integer_2 in [a]:
                        user_integer_2 = int(
                            input("Player Two : Please select number that has not been selected before \n"))
                    continue

                break


        elif counter == 2:

            b = user_integer


        elif counter == 3:

            while True:
                x = user_integer_2
                print(" Now you have : ", w, ",", x, "\n")


                if counter == 3 and user_integer_2 == a or user_integer_2 == w or user_integer_2 == b:

                    if user_integer_2 in [a, w, b]:
                        user_integer_2 = int(
                            input("player_two : Please select number that has not been selected before \n"))
                        continue
                break

        elif counter == 4:

            c = user_integer


        elif counter == 5:

            while True:
                y = user_integer_2
                print(" Now you have : ", w, ",", x, ",", y, "\n")


                if counter == 5 and user_integer_2 == a or user_integer_2 == w or user_integer_2 == b or user_integer_2 == x or user_integer_2 == c:

                    if user_integer_2 in [a, w, b, x, c]:
                        user_integer_2 = int(
                            input(" player_two 5: Please select number that has not been selected before \n"))
                        continue
                break


        elif counter == 6:

            d = user_integer


        elif counter == 7:

            while True:

                z = user_integer_2
                print(" Now you have : ", w, ",", x, ",", y, ",", z, "\n")

                if counter == 7 and user_integer_2 == a or user_integer_2 == w or user_integer_2 == b or user_integer_2 == x or user_integer_2 == c or user_integer_2== y or user_integer_2 == d:

                    if user_integer_2 in [a, w, b, x, c, y, d]:
                        user_integer_2 = int(
                            input(" player_two : Please select number that has not been selected before\n"))
                        continue
                break

        elif counter == 8:
            e = user_integer

        counter = counter + 1

    print("\n")
    if a + b + c == 15 or a + b + d == 15 or a + b + e == 15 or a + c + d == 15 or a + c + e == 15 and w + x + y == 15 or w + x + z == 15 or w + y + z == 15:
        print(" PLAYER-ONE AND PLAYER-TWO ARE THE WINNERS , SO THE GAME IS IN DRAW CASE ")

    elif a + b + c == 15 or a + b + d == 15 or a + b + e == 15 or a + c + d == 15 or a + c + e == 15:
        print("*** PLAYER-ONE IS THE WINNER , CONGRATULATIONS ***\n")
    elif w + x + y == 15 or w + x + z == 15 or w + y + z == 15:
        print("*** PLAYER-TWO IS THE WINNER , CONGRATULATIONS ***\n")
    else:
        print("*** THE GAME IS IN DRAW CASE ***")


while True:
    print("A) Start game\n""B) Exit program")
    choice1 = input("Please enter your choice (A/B):\n").upper()
    if choice1 == "A":
        game()
        print (" Do you want to play again ? \n")
    elif choice1 == "B":
        print("Exit programe")
        break
    else:
        print("Please select a valid choice")