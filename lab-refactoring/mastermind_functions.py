# Import the random library
import random

# Define a function to ask the player to choose 4 colours between blue, green, orange, pink, red, yellow
def ask_player(computer_tuple, player, colours):
    """This function asks the player to choose 4 colours between blue, green, orange, pink, red, yellow
"""
    for i in range(len(computer_tuple)):
        player[i] = input(f"Choose a colour (blue, green, orange, pink, red or yellow) for position number {i + 1}: ")
        while player[i] not in colours:
            print(
                "Wrong entry. Please enter a colour (no space, all small letters) from blue, green, orange, pink, red and yellow")
            player[i] = input(
                f"Choose a colour (blue, green, orange, pink, red or yellow) for position number {i + 1}: ")


# Define a random generator function to generate the computer choice of colours and positions
def random_colour(colours):
    """ This function generates the computer choice of colours and positions"""
    a = [random.choice(colours) for i in range(4)]
    return a



# Define a function to give the result of a round:
## Black means the right colour in the right position
## White means this colour is present in the computer choice but in the wrong position


def give_result(computer_tuple, player):
    """ This function gives the result of a round:
Black means the right colour in the right position
White means this colour is present in the computer choice but in the wrong position"""
    result = ["nothing", "nothing", "nothing", "nothing"]
    computer = list(computer_tuple)
    computer_bis = computer
    for i in range(len(player)):
        # Check if there are any Blacks in the results and add it to the list [b]
        if player[i] == computer[i]:
            result[i] = "black"
            computer_bis[i] = "taken"
    for i in range(len(player)):
        # Check if there are any Whites in the results and add it to the list [b]
        for j in range(len(computer)):
            if player[i] == computer_bis[j]:
                result[i] = "white"
                computer_bis[j] = "taken"
                break
    print(f"\nThe result is {result}\n")
    return result
