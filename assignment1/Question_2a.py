#----------------------------- Question 2 ----------------------------#
'''

Assume s is a string of numbers.

Write a program that prints the longest substring of s in which the
numbers occur in descending order. For example, if
 s = '561984235870154755310', then your program should print

    Longest substring in numeric descending order is: 755310

In the case of ties, print the first substring. For example, if s = '742951', then your program should print

    Longest substring in numeric descending order is: 742

'''

# Functions
import random

def string_of_numbers(length=15):
    """ Return a string of random numbers to length specified
        Defaults to a length of 15 """
    return_string = ""
    for loop in range(length):
        return_string += str(random.randint(0,9))

    return return_string


first_pass = True
test_string = "561984235870154755310"


# Loop until user exits
while True:

    if first_pass:
        print("Test with known string value")
        number_string = test_string
        first_pass = False
    else:
        # Accept input from the user.
        string_length = input("How long would you like the " +
                              "string of numbers to be ('Q' to quit):")

        # Test the input to make sure numbers were entered or exit if Q
        try:
            # First test to see if user entered both values
            if string_length:
                if string_length.upper()[0] == "Q":
                    break
                string_length = int(string_length)
                # Get the string of numbers
                number_string = string_of_numbers(string_length)
            else:
                # Get the string of numbers
                number_string = string_of_numbers()

        # The exception to run if the valid value check failed
        except ValueError:
            print(f"The value you entered ({string_length})",
                   "isn't a number.\nPlease try again...")

    # Print value to be checked
    print(number_string)

    # Start and end pointers
    start_pos = 0
    check_pos = 0
    end_pos = 1
    descending_list = []

    # Determine the descending values
    while end_pos <= (len(number_string)-1):
        descending_list.append((number_string[start_pos:end_pos],end_pos-start_pos))
        if number_string[check_pos] < number_string[end_pos]:
            check_pos = end_pos
            start_pos = check_pos
            end_pos += 1
        else:
            check_pos += 1
            end_pos += 1
    # Append last value
    descending_list.append((number_string[start_pos:end_pos],
                            end_pos-start_pos))

    # Scan the list for the highest length value
    max_length = 0
    longest_string = ""
    for descending_number in descending_list:
        if descending_number[1] > max_length:
            longest_string = descending_number[0]
            max_length = descending_number[1]

    # Use a control break structure to handle the length comparisons
    print("Longest substring in numeric descending order is:",
          longest_string,"\n")


#------------------------- End of Question 2 -------------------------#
