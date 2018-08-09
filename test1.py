squares2 = [i**2 for i in range(1,101)]

print(squares2)



# Imports
from random import randint

# Function definitions
def string_of_numbers(length=15):
    """ Return a string of random numbers to length specified
        Defaults to a length of 15 """

    return_string = ""

    number_list = [str(randint(0,9)) for loop in range(length)]

    return return_string.join(number_list)


#------------------------- Main code ----------------------------#

# Initialise the list of strings to be searched
search_strings = []
# Add a search string to the list with the string_of_numbers function
search_strings.append(string_of_numbers(10))
search_strings.append(string_of_numbers())  # This uses the default of 15
search_strings.append(string_of_numbers(20))

print(search_strings)
