# Question 1
# Write a program that takes input from the user and when the user
# press enter to quit the program gives the sum of all even numbers
# and the sum of all odd numbers.

# Sample Input :
# Enter a number 2
# Enter a number 4
# Enter a number 3
# Enter a number 5
# Enter a number (enter)

# Sample Output :
# Sum of even number: 6
# Sum of odd number: 8


print("-------------- Question 1 -------------")
# Set running flag
running = True
number_list = []
sum_of_even = 0
sum_of_odd = 0

# Loop continues until running is set to False
while running:
    # Accept input from the user.
    number_entered = input("Enter number or leave empty to finish : ")
    # Test the input to make sure it is a value we want
    try:
        # First test to see if user wants to quit entering
        if not number_entered:
            break
        # Next check if the value of the entry is and integer
        val = int(number_entered)
        number_list.append(val)
        # Use the mod function to test if the number is even
        # increment the correct counter
        if val % 2 == 0:
            sum_of_even += val
        else:
            sum_of_odd += val
    # The exception to run if the valid value check failed
    except ValueError:
        print(f"The value you entered ({number_entered}) " +
              "isn't an integer.\nPlease try again...")

# Print the list entered by the user
print("The following numbers were entered:")
print(number_list)

# Print the even and odd statement
print(f"\nSum of even numbers: {sum_of_even}\n" +
      f"Sum of odd numbers: {sum_of_odd}")
print("---------- End of question 1 ----------\n\n")


# Question 2
# Write a program to take a string as input and your program should:
# Print the same string with all lowercase letters.
# Note:  You should not use islower() function.
# Print the number of vowels  ‘aeiou’ present in the string.

print("-------------- Question 2 -------------")
string_entered = input("Enter a word or phrase: ")

# Check if anything was entered before processing the string
if not string_entered:
    print("Nothing was entered.")
else:
    string_in_lowercase = string_entered.lower()

    vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
    # Count the vowels in the string
    for letter in string_in_lowercase:
        if letter in vowels:
            vowels[letter] += 1

    print(f"You entered: {string_entered} ")
    print(f"The same string in lowercase is : {string_in_lowercase} ")
    for vowel in vowels:
        print(f"Vowel:{vowel} ( {vowels[vowel]} occurances )")

print("---------- End of question 2 ----------\n\n")


# Question 3
# Write a program to ask input from the user the number of asterisk
# to print and how many lines need to be printed.

# Sample:
# Input
# Enter number of asterisk: 7
# Enter number of lines: 4

# Output
# *******
# *******
# *******
# *******

print("-------------- Question 3 -------------")
# Accept input from the user.
number_asterisk = input("Enter the number of asterisk : ")
number_lines = input("Enter the number of lines : ")

# Test the input to make sure numbers were entered
try:
    # First test to see if user entered both values
    if number_asterisk and number_lines:
        # Next check if the value of the entry is and integer
        asterisk = int(number_asterisk)
        lines = int(number_lines)
        for line in range(1,lines+1):
            print("*" * asterisk)
    elif (not number_asterisk) and (not number_lines):
        print("You left the number of both value blank")
    elif not number_asterisk:
        print("You left the number of asterick value blank")
    else:
        print("You left the number of lines value blank")
# The exception to run if the valid value check failed
except ValueError:
    print(f"One of the values you entered ({number_asterisk}",
          f"or {number_lines})",
           "isn't an integer.\nPlease try again...")

print("---------- End of question 3 ----------\n\n")


# Question 4
# Write a program to check whether the user input number is
# a prime number or not.

# Sample:
# Input
# Enter number: 8
# Output
# Number 8 is not prime number.

# This solution was inspired by an article at this location:
# https://www.programiz.com/python-programming/examples/prime-number

# Factors that make a number prime.
# It is a natural number above 1 divisible only by itself and 1

# Accept input from the user.
number = input("Enter the number to check for prime factor : ")


try:
    # Check for entry
    if number:
        # Convert to integer
        number = int(number)

        # Check if number greater than 1
        if number > 1:
            # Discard even numbers > 2
            if number > 2 and number%2==0:
                print(f"Number {number} is not a prime number")
            else:
                # Only need to check odd numbers below the square root
                for check in range(3,int(number**(0.5)),2):
                    if (number%check==0):
                        print(f"Number {number} is not a prime number")
                        break
                else:
                    print(f"Number {number} is a prime number")
        else:
            # Must be greater than 1
            print(f"Number {number} is not a prime number by definition")

    else:
        print("Nothing was entered.")

# The exception to run if the valid value check failed
except ValueError:
    print(f"The value you entered ({number}) " +
          "isn't an integer.\nPlease try again...")

print("---------- End of question 4 ----------\n\n")


# Question 5
# Write a program to print the numbers in the following format:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Create variables to allow for easy modification
number_list = []
from_number = 1
to_number = 5

# Loop through the number range
for list in range(from_number,to_number+1):
    # Append the number to the list
    number_list.append(list)
    # Loop through the number_list to the outer iterator value
    for loop in range(0,list):
        # Print the number list index value
        print(number_list[loop], end=' ')
        # If the loop equals the outer iterator less one
        if loop == list-1:
            # Print a new line
            print()


print("---------- End of question 5 ----------\n\n")


# Question 6
# Write a program that accepts a sentence and calculate the
# number of letters and digits.
# Suppose the following input is supplied to the program:
# hello class! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


print("-------------- Question 6 -------------")
# Initilise variables
count_digits = 0
count_letters = 0
count_others = 0

string_entered = input("Enter a word or phrase: ")

# Check if anything was entered before processing the string
if not string_entered:
    print("Nothing was entered.")
else:
    # Count the letters and numbers in the string
    for letter in string_entered:
        if letter.isdigit():
            count_digits += 1
        elif letter.isalpha():
            count_letters += 1
        else:
            count_others += 1

    print(f"Letter count is: {count_letters} ")
    print(f"Digit count is: {count_digits} ")

print("---------- End of question 6 ----------\n\n")
