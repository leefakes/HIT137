#----------------------------- Question 1 ----------------------------#
"""

Assume s is a string of numbers.
Write a program that checks the string s for the values '2', '3', '5'
and '7'.  When one of the values is found in the string, record its
position within the string and continue to check for more occurrences.

Finally, output the results found.

For example, if s = '568714523645873', your program should print:

    2 - 7
    3 - 8 14
    5 - 0 6 11
    7 - 3 13

Give Five (5) different examples with its output.


"""

# Imports
from random import randint


# Function definitions
def string_of_numbers(length=15):
    """ Return a string of random numbers to length specified
        Defaults to a length of 15 """

    return_string = ""
    for loop in range(length):
        return_string += str(randint(0,9))

    return return_string


# ------------------------- Main code ----------------------------#

# Initialise the list of strings to be searched
search_strings = []
# Add this string as a test string with known values
search_strings.append("568714523645873")
# Add a search string to the list with the string_of_numbers function
search_strings.append(string_of_numbers(10))
search_strings.append(string_of_numbers())  # This uses the default of 15
search_strings.append(string_of_numbers(20))
search_strings.append(string_of_numbers(30))

# Loop through each string and count search terms
for search_string in search_strings:
    # Print seperator
    print("-"*30)
    # Print string to be searched
    print("The string to be searched is:")
    print(search_string, "(", len(search_string), ")\n")
    # Print heading for searches
    print("No. Index positions found")
    # Dictionary of values to search for and reset positions to blank
    search_term = {"2":[],"3":[],"5":[],"7":[]}

    # Loop through the search for criteria and add positions to the
    # dictionary
    for search in search_term:
        # Set index pointer to 0. Index pointer is used as the starting
        # position in the string for the find method
        index = 0
        # Keep looping until the find returns -1 (not found)
        while True:
            # Set index to position in string where character found
            index = search_string.find(search[0],index)
            # If not found then exit loop
            if index == -1:
                break
            search_term[search].append(index)
            # Increment starting point to next character
            index += 1

        # Print out the search term
        print(search, "- ", end="")
        # Print the not found message if the dictionary list is empty
        if search_term[search] == []:
            print("value not in string", end="")
        # Loop through the dictionary's list and print positions
        for location in search_term[search]:
            print(location, end=" ")
        # Print blank line to provide separation between searches
        print()

#------------------------- End of Question 1 -------------------------#
