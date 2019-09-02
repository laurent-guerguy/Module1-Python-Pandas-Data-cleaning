"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.
The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

# Dictionaries

dict_text_to_number = {
                        'one':    1,
                        'two':    2,
                        'three':  3,
                        'four':   4,
                        'five':   5,
                        'six':    6,
                        'seven':  7,
                        'eight':  8,
                        'nine':   9,
                        'zero':   0
                      }

# screen return

print('Welcome to this calculator!\n')
print('It can add and subtract whole numbers from zero to five')

# screen inputs

first_value =   input('\nPlease choose your first number (zero to five): ')
operator =      input('\nWhat do you want to do? plus or minus: ')
second_value =  input('\nPlease choose your second number (zero to five): ')

# Functions


def convert_to_num(value):
    '''
    This function transforms a string into its corresponding number.
    :param value: string
    :return:  the number corresponding to the string
    '''
    value = dict_text_to_number.get(value)
    return value

# Start calculations


if first_value \
        not in dict_text_to_number.keys() \
        and second_value \
        not in dict_text_to_number.keys():

    print("\n\tI am not able to answer this question. Check your input.")

elif operator != 'plus' and operator != 'minus':

    print("\n\tI am not able to answer this question. Check your input.")

else:

    first_value_conversion = convert_to_num(first_value)
    second_value_conversion = convert_to_num(second_value)
    print(first_value_conversion)
    print(second_value_conversion)
    print(operator)
    if operator == "plus":
        result = first_value_conversion + second_value_conversion
        print("\n\n\t"
              + first_value.capitalize()
              + " + "
              + second_value
              + " = "
              + str(result))
    else:
        result = first_value_conversion - second_value_conversion
        print("\n\n\t"
              + first_value.capitalize()
              + " - "
              + second_value
              + " = "
              + str(result))

print("\n\nThanks for using this calculator, goodbye :)")



