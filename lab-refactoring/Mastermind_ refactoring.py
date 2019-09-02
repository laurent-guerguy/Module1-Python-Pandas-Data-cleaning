# Mastermind game player vs computer

# Import libraries to be used in the code below
import random
# Import all the functions used in the program by import the mastermind_functions library
import mastermind_functions


# Set the variables respectively for the choice of the computer, the choice of the player, the number of rounds
# and define the colours available.
computer = []
player = ["", "", "", ""]
round_number = 10
colours = ["blue", "green", "orange", "pink", "red", "yellow"]


# Define the colours chosen by the computer

## The result of randomColour is a list that I transform to a tuple called computer_tuple so it stays unchanged as a
## reference for the initial computer choice of colours.
## NOTE: The computer variable is modified during the giveResult function (for reasons I don't have time to solve
## now). That is why I need to create and use computer_tuple.
computer_tuple = tuple(mastermind_functions.random_colour(colours))


# Define the choice of the computer
# computer = mastermind_functions.random_colour()

# Play the game. The game is composed of a maximum of 10 rounds. if after 10 rounds the user has not found the
# computer's choice then the computer wins
for i in range(10):
    print(f"This is round number {i + 1}")
    mastermind_functions.ask_player(computer_tuple, player, colours)
    result2 = mastermind_functions.give_result(computer_tuple, player)
    if result2 == ["black", "black", "black", "black"]:
        print("Congratulations! You won!!")

if result2 != ["black", "black", "black", "black"]:
    print(f"Sorry but you lost. The answer was {computer_tuple}")