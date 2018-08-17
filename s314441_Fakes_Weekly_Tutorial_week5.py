"""
Week 5 – Tutorials
Question 1
Write a Python function to check whether a number is in a given range
"""
def number_in_range(value_to_check, endpoint1, endpoint2) -> bool:
    """ Return a true or false if a number is between two endpoints"""
    # Check which endpoint is the higher number
    if endpoint1 < endpoint2:
        # check if number is between the two endpoints
        return (endpoint1 <= value_to_check <= endpoint2)
    else:
        return (endpoint2 <= value_to_check <= endpoint1)


# Get user values as floats
number = float(input("Enter a number to check: "))
lower_range = float(input("Enter the lower number of the range: "))
upper_range = float(input("Enter the upper number of the range: "))

# Print result of function
if number_in_range(number, lower_range, upper_range):
    print(number, "is between", lower_range, "and", upper_range)
else:
    print(number, "is NOT between", lower_range, "and", upper_range)


"""
2.  Write a Python function that accepts a string and calculate the number
    of upper case letters and lower case letters.

Sample String : 'The Quick Brow '
Expected Output :
    No. of Upper case characters : 3
    No. of Lower case Characters : 12
"""
def case_count(words=""):
    """Print the count of upper and lowercase letters """
    # Initialise counters
    upper_case_letters = 0
    lower_case_letters = 0
    # Check the string exists
    if words:
        # Loop over the string and count case of letters
        for letter in words:
            # Check case of letter
            if letter.isupper():
                # Increment upper counter
                upper_case_letters += 1
            else:
                # Increment upper counter
                lower_case_letters += 1
    # Print results
    print("The phrase:", words, "is", len(words), "characters long")
    print("No. of Upper case characters :", upper_case_letters)
    print("No. of Lower case characters :", lower_case_letters)
    return


phrase = input("Enter phrase to count case of letters:")
case_count(phrase)


"""
3.  Write a Python function that takes a list and returns a new list
with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


"""
4.  Try the following code and rectify the mistakes in the code

def doSum(alist):
    suval = 0
    for l in alst:
        sumval = sumval + l
    return sumval

mylist = [1,2,3,4,5]
print(dSum(mylist))
"""


def do_sum(alist):
    sumval = 0
    for list_item in alist:
        sumval = sumval + list_item
    return sumval


my_list = [1, 2, 3, 4, 5]
print(do_sum(my_list))
