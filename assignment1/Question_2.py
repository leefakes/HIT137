#----------------------------- Question 2 ----------------------------#
"""
Assume s is a string of numbers.

Write a program that prints the longest substring of s in which the
numbers occur in descending order. For example, if
 s = '561984235870154755310', then your program should print

    Longest substring in numeric descending order is: 755310

In the case of ties, print the first substring.

For example, if s = '742951', then your program should print
    Longest substring in numeric descending order is: 742


"""
# Imports
import random


# Function definitions
def string_of_numbers(length=15):
    """ Return a string of random numbers to length specified
        Defaults to a length of 15 """
    return_string = ""
    for loop in range(length):
        return_string += str(random.randint(0, 9))

    return return_string


#------------------------- Main code ----------------------------#
# First use known values
test_string_list = []
test_string_list.append("561984235870154755310")
test_string_list.append("742951")

# Edge case tests
test_string_list.append("")
test_string_list.append("1")
test_string_list.append("222222222")
test_string_list.append("3456789")
test_string_list.append("987654321")
test_string_list.append("123456765432102345654321")

# Now add random numbers 40 characters long
for _ in range(3):
    test_string_list += [string_of_numbers(40)]

# Big number test
test_string_list.append(string_of_numbers(1000))

# Loop until user exits
for number_string in test_string_list:

    # Print value to be checked
    print(number_string)

    # Start and end pointers
    start_pos = 0
    check_pos = 0
    end_pos = 1
    descending_list = []

    # Determine the descending values

    # Loop until the end position index is at the end of the string
    while end_pos <= (len(number_string)-1):
        # Slice the number string and count the length
        descending_list.append(
            (number_string[start_pos:end_pos], end_pos-start_pos))

        # If the next number is smaller than the previous
        if number_string[check_pos] < number_string[end_pos]:
            # Increment the position pointers
            check_pos = end_pos
            start_pos = check_pos
            end_pos += 1
        else:
            # Reset the pointers to check the next pair
            check_pos += 1
            end_pos += 1
    # Append last value
    descending_list.append((number_string[start_pos:end_pos],
                            end_pos-start_pos))

    # Scan the list for the largest length value
    max_length = 0
    longest_string = ""
    for descending_number in descending_list:
        if descending_number[1] > max_length:
            # Set the string and length values
            longest_string = descending_number[0]
            max_length = descending_number[1]

    # Print the longest descending string
    print("Longest substring in numeric descending order is:",
          longest_string, "\n")


#------------------------- End of Question 2 -------------------------#
