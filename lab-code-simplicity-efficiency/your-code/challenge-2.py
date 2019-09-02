"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random
import string
import sys

# Functions


def word_generator(number_of_positions):
    string = ''
    for position in number_of_positions:
        string += random.choice(string.ascii_lowercase + string.digits)
    return string


def list_generator(number_of_strings, min_length=8, max_length=12):
    list_of_words = []
    for i in range(number_of_strings):
        strings_to_generate = None
        if min_length < max_length:

            strings_to_generate = random.choice(range(min_length, max_length))

        elif min_length == max_length:

            strings_to_generate = min_length
        else:

            sys.exit('Incorrect min and max string lengths. Try again.')

        list_of_words.append(word_generator(strings_to_generate))

    return list_of_words

# Inputs

min_length = input('Enter minimum string length: ')
max_length = input('\nEnter maximum string length: ')
number_of_strings = input('\nHow many random strings to generate? ')

# Output

print(list_generator(
                     int(number_of_strings),
                     int(min_length),
                     int(max_length)
                    )
      )

