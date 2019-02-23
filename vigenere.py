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
        text = re.sub(r'[^a-zA-Z]', '', text).lower()
        return text
    except FileNotFoundError:
        print("Could not find file source " + file_name + "\n")
        print("Exiting program...please check if the file is in the current directory.")
        exit(0)


# Formula C[i] = (p[i] + k[i]) mod 26
# c = cipher
# p = plaintext
# k = key
def lowercase_encryption(plaintext_input, key_input):
    encrypted_text = ""
    len_key = len(key_input)
    for i in range(len(plaintext_input)):
        p = ord(plaintext_input[i]) - OFFSET_LOWERCASE
        k = ord(key_input[i % len_key]) - OFFSET_LOWERCASE
        c = (p + k) % 26
        encrypted_text = encrypted_text + chr(c + OFFSET_LOWERCASE)
    return encrypted_text


def main():
    # Grab information before starting encryption process
    print("Program assumes files are in the current directory!\n")
    plaintext = file_information(input("Plaintext file name: "))
    key = file_information(input("Key file name: "))
    key_length = len(key)
    plaintext_length = len(plaintext)
    modified_string = ""

    # Calculate necessary padding if below 512 characters
    if plaintext_length < MAX_FILE_SIZE:
        padding = key_length - (plaintext_length % key_length)
        should_pad = padding > 0
        print("Amount to pad:", padding)
        #c = 1

        # Modify the plaintext so its padded to MAX_FILE_SIZE
        for i in range(plaintext_length + padding):
            if not should_pad and i >= plaintext_length or should_pad and i >= MAX_FILE_SIZE:
                print("reached break statement")
                break
            elif should_pad and i >= plaintext_length:
                #print("padding count:", c)
                #c += 1
                modified_string = modified_string + "x"
            else:
                modified_string = modified_string + plaintext[i]
    elif plaintext_length > MAX_FILE_SIZE:
        # Modify the plaintext so its only the MAX_FILE_SIZE
        for i in range(MAX_FILE_SIZE):
            modified_string = modified_string + plaintext[i]

    plaintext_length = len(modified_string)
    print("PL:", plaintext_length)
    print("KL:", key_length)

    plaintext = modified_string
    cipher = lowercase_encryption(plaintext, key)

    print("Key:", "\n\n" + formatted_print(key))
    print("\nPlaintext:", "\n\n" + formatted_print(plaintext))
    print("\nCiphertext:", "\n\n" + formatted_print(cipher))

    pass


if __name__ == '__main__':
    main()
