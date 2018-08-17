"""

Tutorial – Week 4

1.  Write a loop that accumulates the sum of all of the numbers in a
list named data.


"""

# Question 1
import random

qty_of_numbers = 10

# let us fill the data list with a loop of random numbers
data = []
for number in range(qty_of_numbers):
    data.append(random.randint(0, 99))
# Accumulate sum of numbers
total = 0
for number in data:
    total += number
# Print data and total
print(data, "\n", total)


"""
2.  Define a function named sum. This function expects two numbers, named
low and high, as arguments. The function computes and returns the sum of
all of the numbers between low and high, inclusive.

"""
# Question 2

# Define sum function
def sum(low, high) -> int:
    """Return sum of integer values between low and high inclusive"""
    # Check low is less than high
    if low >= high:
        print("The first number must be lower than the second number")
        return None
    # Total accumulator
    total = 0
    # Perform loop
    for number in range(low, high+1):
        # Accumulate total
        total += number
    return total


# Loop continues until break is executed
while False:
    # Accept input from the user.
    first_entry = input("Enter first of two numbers: ")
    second_entry = input("Enter second of two numbers: ")

    # Test the input to make sure numbers were entered
    try:
        # First test to see if user entered both values
        if first_entry and second_entry:
            # Next check if the value of the entry is and integer
            print(sum(int(first_entry), int(second_entry)))
            break
        elif (not first_entry) and (not second_entry):
            print("You left the number of both value blank")
        elif not first_entry:
            print("You left the number of asterick value blank")
        else:
            print("You left the number of lines value blank")
    # The exception to run if the valid value check failed
    except ValueError:
        print("One of the values you entered (",first_entry,
              ") or ", second_entry, ")",
              "isn't an integer.\nPlease try again...")

"""
3.  Assume that the variable data refers to the dictionary
            {“b”:20, “a”:35}.
Write the expressions that perform the following tasks:
a.  Replace the value at the key “b” in data with that value’s negation.
b.  Add the key/value pair “c”:40 to data.
c.  Remove the value at key “b” in data, safely.
d.  Print the keys in data in alphabetical order.

"""
# Assign dictionary values to data
data = {"b":20, "e":35, "a":98}
print(data)

# Change the value. If the key is present then the value is updated
data["b"] = -(data["b"])
print(data)

# Add a key value pair. If the key is not present it will be added
data["c"] = 40
print(data)

# Remove
del(data["b"])
print(data)

# The sorted function returns the data list for printing
print(sorted(data))


"""
4.  Write a Python program to get the smallest number from a list

    Assumption is that the min function should not be used, otherwise it
    will be a one line program :-)

"""


def smallest_number_from_list(number_list=None):
    """ Return the smallest value from the list or None if
        list not passed """

    smallest = None
    if number_list:
        smallest = number_list[0]
        # Scan through list and find smallest number
        for number in number_list:
            if smallest > number:
                smallest = number
    return smallest


# Main program
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 99))

print(test_list)
print(smallest_number_from_list(test_list))


"""
5.  Write a Python script to concatenate following dictionaries to create
a new one
    Sample Dictionary :
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)
