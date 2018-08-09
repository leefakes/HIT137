#----------------------------- Question 4 ----------------------------#
"""

Write a python program that allows the user to navigate the lines of
text in a file. The program should prompt the user for a filename and
input the lines of text into a list. The program then enters a loop in
which it prints the number of lines in the file and prompts the user for
a line number. Actual line numbers range from 1 to the number of lines
in the file. If the input is 0, the program quits. Otherwise,the
program prints the line associated with that number.


"""

# Module contains object methods for checking file existance
import pathlib

# Ask user for filename
filename = input("Enter name for the file: ").strip().lower()

# Check if filename provided
if filename:
    # Check if file exists and is accessible
    file_check = pathlib.Path(filename)
    if file_check.is_file():
        # Open file for read only
        file = open(filename,'r')
        # Read the lines from the file into memory
        lines = file.read().split("\n")
        # Close the file
        file.close()
        # Print the number of lines in the file
        range_high = len(lines)-1
        # Set up a while loop to allow user to navigate file contents
        while True:
            # Print instructions
            print("\nEnter a line number between 1 and",range_high,
                  ": to display the line or zero (0) to exit.")
            display_line = input("Line number: ")
            # Check if display_line is numeric and not 0
            try:
                # First test to see if user wants to quit entering
                if display_line:
                    display_line = int(display_line)
                    if display_line == 0:
                        break
                    elif display_line > range_high:
                        # Print error message for user feedback
                        print("The line number is more than",
                              range_high,
                              "\nPlease try again...")
                    elif display_line < 0:
                        print("The line number is less than 0",
                              "\nPlease try again...")
                    else:
                        print("\n",lines[display_line-1])
                else:
                    # Print error message for user feedback
                    print("You left the line number blank.",
                          "\nPlease try again...")

            # The exception to run if the valid value check failed
            except ValueError:
                print(f"The value you entered ({display_line}) " +
                      "isn't an integer.\nPlease try again...")
    else:
        print("Filename doesn't exist")
else:
    print("Filename cannot be blank")


#------------------------- End of Question 4 -------------------------#
