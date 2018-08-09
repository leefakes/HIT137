#----------------------------- Question 5 ----------------------------#
"""

Write a program that encrypts and decrypts the user input.  Note – Your input should be only lowercase characters with no spaces.
Your program should have a secret word that will be used for encryption/decryption.  Each character of the user’s input should be offset by the value of the same character in your secret word.  For example, if my secret word is “cab” and the user wants to encrypt “apples”.
c   a   b   c   a   b
3   1   2   3   1   2

a   p   p   l   e   s
1   16  16  12  5   19

4   17  18  15  6   21
d   q   r   o   f   u

The encrypted output would be “dqrofu”.
The program should ask the user for input to encrypt, and then display the resulting encrypted output.  Next your program should ask the user for input to decrypt, and then display the resulting decrypted output.
Enter phrase to Encrypt (lowercase, no spaces):  apples
Result: dqrofu

Enter phrase to Decrypt (lowercase, no spaces):  dqrofu
Result: apples


"""

# Initialize secret key
secret_key = "cvexfygjknpqs"
# Use this alphabet - this includes allowed punctuation
# The position of the space in the alphabet must be tested if either
# the alphabet or key are changed to ensure that an encrypted value
# cannot be created with a leading space.
alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet = ")a bc?def$ghi!jkl:mnopqr;stu,vwx(yz.'0123456789"
# If secret_key or alphabet are changed then ensure to run the below
# to check that the leading character of the encrypted text cannot be
# a space.
# for letter in alphabet:
#    encrypted = vigenere_message(letter,secret_key,"E")
#    print("Clear Message:",letter, "Encrypted :", encrypted)


def vigenere_message(message_text,secret_key,encryption_type="E"):
    """Encrypt or decrypt the message text with secret key
       using the vigenere cipher algorithm and return encrypted value"""

    # This error should only occur if the calling code is wrong.
    assert encryption_type in ["E","D"], \
                "Encryption type is required and may only " + \
                "be '(E)ncrypt' or '(D)ecrypt'"

    # Strip leading and trailing spaces from message and ensure message
    # is lowercase
    message_text = message_text.strip().lower()

    # Create encrypted value by adding characters together
    encrypt_list = ""
    # Secret_key position
    secret_key_position = 0
    # Loop through each character of message
    for character in message_text:
        # Find letter
        index = alphabet.find(character)
        # Check that the character was found or return the plain character
        if index > -1:
            # Find the secret_key index
            secret_index = alphabet.find(secret_key[secret_key_position])

            if encryption_type == "E":
                # When encrypting we add the secret index
                index += secret_index
            else:
                # When decrypting we subtract the secret index
                index -= secret_index

            # Wrapping the index through the alphabet string
            index %= len(alphabet)
            # Add character to list
            encrypt_list += alphabet[index]

            # Increment secret_key position
            secret_key_position += 1
            # Wrap the key position at the length of the secret_key
            secret_key_position %= len(secret_key)

    # Convert the encrypted list to text
    return encrypt_list


# Prints a banner and instructions
print("#"*80)
print("#"," "*76,"#")
print("#","Encrypt/Decrypt".center(76),"#")
print("#"," "*76,"#")
print("#","Type 'E' to encrypt a string".center(76),"#")
print("#","Type 'D' to decrypt a string".center(76),"#")
print("#","Type 'Q' to quit".center(76),"#")
print("#"," "*76,"#")
print("#"*80)

# Enter while loop
while True:

    # Get user input and limit to
    operation = input("Option: ").strip().lower()[:1]

    if operation:
        if operation == "q":
            break
        elif operation =="e":
            message = input("Enter phrase to Encrypt " +
                            "(lowercase, no spaces): ")
            encrypted = vigenere_message(message,secret_key,"E")
            print("Result :", encrypted)
        else:
            message = input("Enter phrase to Decrypt " +
                            "(lowercase, no spaces): ")
            decrypted = vigenere_message(message,secret_key,"D")
            print("Result:",decrypted)
    else:
        print("Incorrect entry please try again")


#------------------------- End of Question 5 -------------------------#
