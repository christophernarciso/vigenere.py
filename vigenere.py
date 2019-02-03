import re

# LOWERCASE ENCRYPTION IMPLEMENTATION ONLY
# Main script constants
MAX_FILE_SIZE = 512
OFFSET_LOWERCASE = 97


# Return formatted guideline text of 80 characters per line
def formatted_print(text):
    formatted_text = ""
    counter = 0

    for letter in text:
        if counter > 0 and counter % 80 == 0:
            formatted_text = formatted_text + "\n"
        formatted_text = formatted_text + letter
        counter += 1

    return formatted_text


# Return contents of a file
def file_information(file_name):
    try:
        file = open(file_name, "r")
        text = file.read()
        return re.sub(r'[^A-Za-z[0-9]]', '', text).lower()
    except FileNotFoundError:
        print("Could not find file source " + file_name + "\n")
    return


# Formula C[i] = (p[i] + k[i]) mod 26
# c = cipher
# p = plaintext
# k = key
def lowercase_encryption(plaintext_input, key_input):
    encrypted_text = ""
    len_key = len(key_input)
    for i in range(len(plaintext_input)):
        if plaintext_input[i] == ' ':
            break
        p = ord(plaintext_input[i]) - OFFSET_LOWERCASE
        k = ord(key_input[i % len_key]) - OFFSET_LOWERCASE
        c = (p + k) % 26
        encrypted_text = encrypted_text + chr(c + OFFSET_LOWERCASE)
    return encrypted_text


# Grab information before starting encryption process
print("Program assumes files are in the current directory!\n")
plaintext = file_information(input("Plaintext file name: "))
key = file_information(input("Key file name: "))
key_length = len(key)
plaintext_length = len(plaintext)
padding = 0

# Calculate necessary padding if below 512 characters
if plaintext_length < MAX_FILE_SIZE:
    padding = key_length - (plaintext_length % key_length)

