# Question 1
# Write a Python program to find the smallest and largest of three numbers.
# Sample Input : Enter the three numbers : 1,2,3
# Sample Output : Largest : 3  Smallest : 1

print("Question 1 answer 1")
# Add values to the list
number_list = [1,2,3]
print(f"Given the list of numbers: {number_list}")
# Sort the list lowest to highest in case the list is not in order
number_list.sort()
smallest_value = number_list[0]
# Reverse the list highest to lowest
number_list.reverse()
largest_value = number_list[0]
# Print the largest number item. The 'end' parameter allows us to override
# the default behaviour of a newline
print(f"Largest : {largest_value}", end="  ")
# Print the smallest value item
print(f"Smallest : {smallest_value}")
print("End of question 1 answer 1 \n\n")

print("Question 1 answer 2")
# Add values to the list
number_list = [1,2,3]
print(f"Given the list of numbers: {number_list}")
# Get the lowest value
smallest_value = min(number_list)
# Get the highest value
largest_value = max(number_list)
# Print the largest number item.
print(f"Largest : {largest_value}", end="  ")
# Print the smallest value item
print(f"Smallest : {smallest_value}")
print("End of question 1 answer 2\n\n")


# Question 2
# Write a python program that will print the following:
# 1   3   5  7   9  11
# 10 8   6  4   2  0
# (Hint: After 11 the number gets subtracted by 1 then it gets subtracted by 2)

print("Question 2 solution 1 using while and if statements")
# Set counter and flag
i = 1
ascending = True
# Loop will continue until the value of i remains greater than zero
while i > 0:
    # Print value of i
    print(i, end=", ")
    # Test if i = 11 and decrement the value
    if i == 11:
        i -= 1
        ascending = False
        # Print value of i - only occurs once
        print(i, end=", ")
    # Check flag and set value to increment/decrement by
    if ascending:
        step = 2
    else:
        step = -2
    # Increment/Decrement counter
    i += step

# Print the last value of the while loop
print(i)
print("End of question 2 solution 1\n")

print("Question 2 solution 2 using for in and setting value of second range to last number of first")

# Set first loop within the range of 1 and 12. The second parameter
# of range is the stopping value. If the value was 11 then it will
# only print up to 9 so we need to add 1 to prevent the loop
# terminating before we are ready.
# The third parameter is the amount to increment/decrement by
for i in range(1,12,2):
    print(i, end=", ")

# Set the second loop within the range of where the last loop stopped
# which in this case is 11. We subtract one from that value to give us
# the number we need as the starting value 10 and then decrement by 2.
# The stopping value terminates the loop so it needs to be lower than the last number we want to print.
for j in range(i-1,-1,-2):
    if j == 0:
        print(j)
    else:
        print(j, end=", ")

print("End of question 2 solution 2\n\n")


# Question 3
# Write a python program that will accept 10 numbers from the user and find the number of odd and even numbers.
# Sample Input    : 22, 11, 6, 99, 100
# Sample Output: There are 2 odd numbers and 3 odd numbers

print("Question 3")

# Set counters and variables
number_of_values = 10
count_of_even = 0
count_of_odd = 0
number_list = []

# Set the loop to continue until the number of entries equals the
# required number of entries.
while count_of_even + count_of_odd < number_of_values:
    # Accept input from the user.
    number_entered = input(f"Enter number " +
                           f"{count_of_even + count_of_odd + 1} of " +
                           f"{number_of_values} or 'Q' to quit : ")
    # Test the input to make sure it is a value we want
    try:
        # First test to see if user wants to quit entering
        if number_entered.lower() == 'q':
            break
        # Next check if the value of the entry is and integer
        val = int(number_entered)
        number_list.append(val)
        # Use the mod function to test if the number is even
        # increment the correct counter
        if val % 2 == 0:
            count_of_even += 1
        else:
            count_of_odd += 1
    # The exception to run if the valid value check failed
    except ValueError:
        print(f"The value you entered ({number_entered}) " +
              "isn't a number.\nPlease try again...")

# Print the list entered by the user
print(number_list)
# Print the even and odd statement
print(f"There are {count_of_even} even numbers and " +
      f"{count_of_odd} odd numbers")
print("End of question 3\n\n")


# Question 4
# Write a python program that will print the number of days if the user inputs the month name.
# Sample Input    : March
# Sample Output: No of days : 31.

print("Question 4")
# Add months and days to dictionary. This does not account for leap years.
months = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# Set running flag
running = True

# Loop continues until running is set to False
while running:
    # Accept input from user
    input_value = input("Enter the month (minimum 3 characters)" +
                        " or 'Q' to quit:").title()

    # First check that the entered value is 1 character and a 'Q'
    # to allow the user to quit
    if len(input_value) == 1 and input_value == 'Q':
        running = False
    # now check if the length of the string is more than 3
    # since we know that the first 3 characters of the key are
    # unique we can use this to do a partial match of the dictionary key
    elif len(input_value) >= 3:
        # First check if any of the keys have a partial match
        if any(key.startswith(input_value) for key in months):
            # Find value in dictionary
            for key in months:
                if key.startswith(input_value):
                    # Replace input with the key so we can now lookup
                    # in the dictionary without a key error
                    input_value = key
                    # force exit from the loop
                    break
            # print the result of the lookup
            print(f"No of days in {input_value} are {months[input_value]}")
        # Check if we need to end the loop
        else:
            print(f"The value you entered ({input_value}) " +
                  "wasn't in my list.\nPlease try again...")
