from enum import IntEnum, auto


def get_option():
    """Prompt the user to select an option"""
    max_option = max([option.value for option in Option])

    print("""1: Input text to work with
2: Print the current text
3: Encrypt the current text
4: Decrypt the current text
5: Exit """)

    # Repeat until valid input
    is_valid = False
    while not is_valid:
        option = input("Your choice: ")
        try:
            option = int(option)
            if not (0 < option <= max_option):
                raise ValueError
            is_valid = True
        except ValueError:
            print(f"'{option}' is not a valid option." +
                  f" Only numbers 1-{max_option} are acceptable.")
    return option


def input_message():
    """Returns a user submitted message"""
    return input("Your text: ").upper()


def print_message(msg):
    """Prints 'Your text: msg'"""
    print("Your text: " + msg)


def get_char_values(char_idx, key_idx, msg, key):
    """Returns the positions in the alphabet for the characters \
        at position idx in the msg and key """

    # Get the numerical value for the key character
    key_idx = key_idx % len(key)
    key_char = key[key_idx]
    key_char_value = ord(key_char) - ORD_A

    # Get the numerical value for the message character
    msg_char = msg[char_idx]
    msg_char_value = ord(msg_char) - ORD_A

    return msg_char_value, key_char_value


def encrypt(msg, key):
    """Encrypts msg with the key, using Vigenère-cipher"""
    encrypted_msg = ""
    key_idx = 0
    for char_idx, msg_char in enumerate(msg):
        # If the character is a space, don't encrypt it
        if msg_char == " ":
            encrypted_msg += " "
        else:
            # Get the values for message and key characters
            msg_char_value, key_char_value = get_char_values(
                char_idx, key_idx, msg, key)

            # Get the encrypted letter and add it to the encrypted message
            encr_letter_value = (
                msg_char_value + key_char_value) % LENGTH_ALPHABET
            encr_letter = chr(encr_letter_value + ORD_A)
            encrypted_msg += encr_letter

            key_idx += 1

    return encrypted_msg


def decrypt(msg, key):
    """Decrypts msg with the key, using Vigenère-cipher"""
    decrypted_msg = ""
    key_idx = 0
    for char_idx, msg_char in enumerate(msg):
        # If the character is a space, don't decrypt it
        if msg_char == " ":
            decrypted_msg += " "
        else:
            # Get the values for message and key characters
            msg_char_value, key_char_value = get_char_values(
                char_idx, key_idx, msg, key)

            # Get the decrypted letter and add it to the encrypted message
            decr_letter_value = (
                msg_char_value - key_char_value) % LENGTH_ALPHABET
            decr_letter = chr(decr_letter_value + ORD_A)
            decrypted_msg += decr_letter

            key_idx += 1

    return decrypted_msg


def main():
    """Main method"""
    message = ""
    exit_app = False

    # Repeat until user exits
    while not exit_app:
        # Get an option
        option = get_option()

        if option == Option.INPUT:
            message = input_message()

        elif option == Option.OUTPUT:
            print_message(message)

        elif option == Option.ENCRYPT:
            key = input("Key: ").upper()
            message = encrypt(message, key)

        elif option == Option.DECRYPT:
            key = input("Key: ").upper()
            message = decrypt(message, key)

        elif option == Option.EXIT:
            print("Bye")
            exit_app = True

        print()


class Option(IntEnum):
    INPUT = 1
    OUTPUT = 2
    ENCRYPT = 3
    DECRYPT = 4
    EXIT = 5


ORD_A = ord("A")
LENGTH_ALPHABET = 26

if __name__ == "__main__":
    main()
