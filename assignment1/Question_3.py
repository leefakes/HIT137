#----------------------------- Question 3 ----------------------------#
'''

You have recently returned to Australia after a holiday abroad.  You
have some unspent foreign currency that you need to convert back into
AUD (Australian Dollars).  Write a program that will allow you to enter
two or more amounts of foreign currency and their associated exchange
rate.  Convert the amounts back into AUD and print the total sum of AUD
received once all conversions are complete.

Resulting program output might look similar to:

    Enter currency amount:  100
    Enter exchange rate:  0.75
    100.0000 / 0.7500 = 133.33

    Enter currency amount:  100
    Enter exchange rate:  0.50
    100.0000 / 0.5000 = 200.00

    Total AUD received = $333.33

'''

# Initialise loop variable and accumulators
convert_now = True
exchanged_amount = 0
exchanged_total = 0

# Loop while convert_now is true
while convert_now:
    # Print a line on the screen
    print("\n" + "-"*40)
    # Ask user to enter amount to be converted to AUD
    amount = input("Enter currency amount: ")
    # Ask user for conversion rate
    exchange_rate = input("Enter exchange rate: ")
    # Print a line on the screen
    print("-"*40)

    # Check user input
    try:
        # First test to see if user entered both values
        if amount and exchange_rate:
            # Next check if the value of the entry is a float
            # by attempting to set the amount to a float
            amount = float(amount)
            exchange_rate = float(exchange_rate)
            # Check that exchange rate is not zero
            # otherwise a divide by zero error will occur
            if exchange_rate != float(0):
                # Calculate the echange amount
                exchanged_amount = amount/exchange_rate
                # Accumulate the amount into the total variable
                exchanged_total += exchanged_amount
                # Display the exchanged values
                print("{:-.2f}".format(amount),"/",
                      "{:-.2f}".format(exchange_rate),"=",
                      "{:-.2f}".format(exchanged_amount),"\n")
                print("-"*40)

                # Initialise the yes/no loop variable
                yes_no = ""
                # Loop until a Y or N is provided
                while yes_no not in ["Y","N"]:
                    yes_no = input("Do you wish to add another value?(Y/N)")
                    # We want to check for the first character only
                    # so slice the first character and force it to uppercase
                    yes_no = yes_no.upper()[:1]

                # Set the convert_now switch to true or false
                convert_now = (yes_no=="Y")
            else:
                # Print error message for user feedback
                print("The exchange rate cannot be zero.",
                      "\nPlease try again...")
        elif (not amount) and (not exchange_rate):
            # Print error message for user feedback
            print("You left both values blank.\nPlease try again...")
        elif not amount:
            # Print error message for user feedback
            print("You left the currency amount blank.",
                  "\nPlease try again...")
        else:
            # Print error message for user feedback
            print("You left the exchange rate blank.",
                  "\nPlease try again...")
    # The exception to run if the valid value check failed
    except ValueError:
        # Print error message for user feedback
        print("One of the values you entered (",amount,
              "or",exchange_rate," )isn't a number.",
              "\nPlease try again...")

# Print the total amount to receive when exchanged
print("\n" + "="*40)
print("Total AUD received = {:-.2f}".format(exchanged_total))
print("="*40,"\n")
#------------------------- End of Question 3 -------------------------#
