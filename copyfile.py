# Question 7
# Write a script named copyfile.py. This script should prompt the
# user for the names of two text files. The contents of the first
# file should be input and written to the second file.


filename1 = input("Enter name for first file: ").strip().lower()
filename2 = input("Enter name for second file: ").strip().lower()

if filename1 != filename2:
    # open with 'w' mode will create the file
    file1 = open(filename1,'w')
    # the file objects write method is now used to add content to the file
    file1.write("This is a sentence to be writen to the file")
    # Change the file object mode to read
    file1 = open(filename1,'r')
    # read file contents into variable
    file1_content = file1.read()
    # close the file
    file1.close

    # Open the second file for writing
    file2 = open(filename2,'w')
    # Write the contents to the file
    file2.write(file1_content)
    # Close the file
    file2.close

    print(f"File {filename1} has been created a sentence",
          f"added and this has been written to {filename2}")
else:
    print("Filenames must be different!")
