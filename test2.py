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
                for check in range(3,int(number**(0.5))+1,2):
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
