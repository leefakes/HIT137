#----------------------------- Question 6 ----------------------------#
"""

Write a python program that accepts a text file as input. The program
should read the text file and display all unique words in alphabetical
order.  It should then display the non-unique words and the number of
times that they occurred in the input text.

Input file contains the following text:

  how much wood would a woodchuck chuck if a woodchuck could chuck wood

Expected outcome should resemble:
Non-unique words and number of occurrences in no particular order:
         wood  :  2
         a  :  2
         woodchuck  :  2
         chuck  :  2

Unique words in alphabetic order:
         could
         how
         if
         much
         would

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
        words = file.read().split()
        # Close the file
        file.close()
        # Create dictionary to hold values
        word_counter = {}
        for word in words:
            if word in word_counter:
                word_counter[word] +=1
            else:
                word_counter[word] =1
        # Initialise lists
        single_words = []
        multiple_words = []
        # Scan through the list and place into correct list
        for word in word_counter:
            if word_counter[word] == 1:
                single_words.append(word)
            else:
                multiple_words.append((word,word_counter[word]))

        print("Non-unique words and number of occurrences",
              "in no particular order:")
        for word in multiple_words:
            print(word[0],":",word[1])
        print("\nUnique words in alphabetic order:")
        single_words.sort()
        for word in single_words:
            print(word)

    else:
        print("Filename doesn't exist")
else:
    print("Filename cannot be blank")


#------------------------- End of Question 6 -------------------------#
