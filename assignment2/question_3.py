# Imports
import random


# Function definitions
def list_of_numbers(length=15, random_from=0, random_to=99):
    """ Return a list of random numbers to length specified
        Defaults to a length of 15 """
    return_list = []
    for loop in range(length):
        return_list.append(random.randint(random_from, random_to))

    return return_list


def bubble_sort(number_list):
    # Sort the numbers with bubble sort
    length = len(number_list)
    list_sorted = False
    pass_counter = 0
    switch_count = 0
    while not list_sorted:
        pass_counter += 1
        switch_count = 0
        for number in range(0, length-1):
            list_sorted = True
            left = number_list[number]
            right = number_list[number+1]
            if left > right:
                switch_count += 1
                number_list[number] = right
                number_list[number+1] = left

        # Check termination condition
        list_sorted = (switch_count == 0)

    return (number_list, pass_counter)


# Accept input from the user.
elements = input("Enter the number of list elements to be sorted (10):")
low_range = input("Enter the starting number for random selection (1):")
high_range = input("Enter the last number for random selection (99):")

# if data entry is empty then place default values into variables
if not elements:
    elements = "10"
if not low_range:
    low_range = "1"
if not high_range:
    high_range = "99"

# Test the input to see if user wants to override defaults
try:
    # Try and convert entered values to integers
    elements = int(elements)
    low_range = int(low_range)
    high_range = int(high_range)

    # List of numbers to be sorted
    unsorted = list_of_numbers(elements, low_range, high_range)
    print("\nList to be sorted:", unsorted, '\n')
    sorted_list, passes = bubble_sort(unsorted)
    print("Sorted list:", sorted_list, "sorted in", passes,
          "passes using a bubble sort")

# The exception to run if the valid value check failed
except ValueError:
    print(f"One of the values you entered ({elements}",
          f"or {low_range} or {high_range})",
          "isn't an integer.\nPlease try again...")
