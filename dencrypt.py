import string

ALPHABET = string.ascii_lowercase

def generate_vigenere_matrix():
    matrix = []
    for i in range(len(ALPHABET)):
        row = ALPHABET[i:] + ALPHABET[:i]
        matrix.append(row)
    return matrix

VIGENERE_MATRIX = generate_vigenere_matrix()

def decryptC(message, key):
    decrypted_message = ""
    for c in message:
        if c in ALPHABET:
            position = ALPHABET.find(c)
            decrypted_position = (position - key) % len(ALPHABET)
            decrypted_letter = ALPHABET[decrypted_position]
            decrypted_message += decrypted_letter
        elif c.isupper():
            position = ALPHABET.find(c.lower())
            decrypted_position = (position - key) % len(ALPHABET)
            decrypted_letter = ALPHABET[decrypted_position].upper()
            decrypted_message += decrypted_letter
        else:
            decrypted_message += c
    return decrypted_message

def decryptV(message, key):
    decrypted_message = ""
    full_key = ""
    key_index = 0

    # Формирование full_key
    for char in message:
        if char.lower() in ALPHABET:
            full_key += key[key_index % len(key)].lower()
            key_index += 1

    key_index = 0

    for i in range(len(message)):
        if message[i].lower() in ALPHABET:
            pos_mes = ALPHABET.find(message[i].lower())
            pos_key = ALPHABET.find(full_key[key_index])
            decrypted_letter = ALPHABET[(pos_mes - pos_key) % len(ALPHABET)]

            if message[i].isupper():
                decrypted_letter = decrypted_letter.upper()

            decrypted_message += decrypted_letter
            key_index += 1
        else:
            decrypted_message += message[i]

    return decrypted_message

def main():
    print("Welcome to Caesar & Vigenere decrypt program")

    while True:
        try:
            cipher_type = int(input("Enter 1 for Caesar, 2 for Vigenere: "))
            if cipher_type not in [1, 2]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    path_read = input("Enter path to your encrypted file: ")
    path_write = input("Enter save path for decrypted file: ")

    if not path_read:
        path_read = "output.txt"
    if not path_write:
        path_write = "output2.txt"

    try:
        with open(path_read, 'r') as file:
            message = file.read()
            if not message:
                print("Error: The input file is empty.")
                return
    except FileNotFoundError:
        print(f"Error: The file {path_read} was not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    if cipher_type == 1:
        while True:
            try:
                key = int(input("Enter your Caesar key (integer): "))
                break
            except ValueError:
                print("Error: Key must be an integer.")

        decrypted_message = decryptC(message, key)

    elif cipher_type == 2:
        while True:
            key = input("Enter your Vigenere key (letters only): ")
            if key.isalpha():
                break
            else:
                print("Error: Key must contain letters only.")

        decrypted_message = decryptV(message, key)

    try:
        with open(path_write, 'w') as file:
            file.write(decrypted_message)
    except Exception as e:
        print(f"Error while saving the file: {e}")
        return

    print(f"Decryption completed successfully. Decrypted message saved to {path_write}.")

main()
