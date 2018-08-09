"""

Tutorial – Week 4

1.  Write a loop that accumulates the sum of all of the numbers in a list named data.

2.  Define a function named sum. This function expects two numbers, named low and high, as arguments. The function computes and returns the sum of all of the numbers between low and high, inclusive.


3.  Assume that the variable data refers to the dictionary {“b”:20, “a”:35}. Write the expressions that perform the following tasks:
a.  Replace the value at the key “b” in data with that value’s negation.
b.  Add the key/value pair “c”:40 to data.
c.  Remove the value at key “b” in data, safely.
d.  Print the keys in data in alphabetical order.

4.  Write a Python program to get the smallest number from a list

5.  Write a Python script to concatenate following dictionaries to create a new one
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

!End!

"""

# Question 1
import random

qty_of_numbers = 10

# let us fill the data list with a loop of random numbers
data = []
for number in range(qty_of_numbers):
    data.append(random.randint(0,99))
# Accumulate sum of numbers
total = 0
for number in data:
    total += number
# Print data and total
print(data,"\n",total)


# Question 1 alternate answer
import random

qty_of_numbers = 10

# Or the same code as above in two lines
data = [random.randint(0,99) for _ in range(qty_of_numbers)]
# Print data and total
print(data,"\n",sum(data))


def sum_1(low,high):
    return sum(number for number in range(low,high+1))


def sum(low,high) -> int:
    total = 0
    for number in range(low,high+1):
        total += number
    return total


print(sum_method_2(1,11))
