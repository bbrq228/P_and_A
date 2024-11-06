import string

ALPHABET = string.ascii_lowercase

# таблица для Виженера
def generate_vigenere_matrix():
    matrix = []
    for i in range(len(ALPHABET)):
        row = ALPHABET[i:] + ALPHABET[:i]
        matrix.append(row)
    return matrix

VIGENERE_MATRIX = generate_vigenere_matrix()

def encryptC(message, key):
    encrypted_message = ""
    for c in message:
        if c in ALPHABET:
            position = ALPHABET.find(c)  # нахождение в алфавите номер i
            encrypted_position = (position + key) % len(
                ALPHABET)  # % - деление с остатком. Если будет больше 26, перейдет на начало
            encrypted_letter = ALPHABET[encrypted_position]
            encrypted_message += encrypted_letter
        elif c.isupper():
            position = ALPHABET.find(c.lower())
            encrypted_position = (position + key) % len(ALPHABET)
            encrypted_letter = ALPHABET[encrypted_position].upper()
            encrypted_message += encrypted_letter
        else:
            encrypted_message += c  # добавление оставшиеся символы без изменений
    return encrypted_message


def encryptV(message, key):
    encrypted_message = ""
    full_key = ""
    key_index = 0  # индекс для отслеживания текущего символа ключа

    # Формирование full_key, игнорируя пробелы и не алфавитные символы
    for char in message:
        if char.lower() in ALPHABET:
            full_key += key[key_index % len(key)].lower()
            key_index += 1  # увеличение индекса ключа только для букв

    # Индекс для шифрования
    key_index = 0

    for i in range(len(message)):
        if message[i].lower() in ALPHABET:  # проверка, является ли символ буквой
            pos_mes = ALPHABET.find(message[i].lower())
            pos_key = ALPHABET.find(full_key[key_index])
            encrypted_letter = VIGENERE_MATRIX[pos_mes][pos_key]

            # Для заглавных:
            if message[i].isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_message += encrypted_letter  # добавление зашифрованной буквы
            key_index += 1
        else:
            encrypted_message += message[i]  # добавление символов без изменений

    return encrypted_message


def main():
    print("Welcome to Ceaser & Vigenere encrypt program")

    # Проверка ввода типа шифра
    while True:
        try:
            cipher_type = int(
                input("Enter 1 if you want to use the Caesar's cipher or 2 to use the Vigenère's cipher: "))
            if cipher_type not in [1, 2]:
                raise ValueError("Invalid choice. Please enter 1 or 2.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    path_read = input("Enter path to your file: ")
    path_write = input("Enter save path to your file: ")

    if path_read == "":  # если оставить поле ввода пустым, то автоматически сохранит в output и прочтет input
        path_read = "input.txt"
    if path_write == "":
        path_write = "output.txt"

    try:
        with open(path_read, 'r') as file:
            message = file.read()  # файл читается целиком
            if not message:
                print("Error: The input file is empty.")
                return
    except FileNotFoundError:
        print(f"Error: The file {path_read} was not found.")
        return
    except Exception as e:
        print(f"Error: {e}")
        return

    # Обработка неверного ввода ключа для Цезаря
    if cipher_type == 1:
        while True:
            try:
                key = int(input("Enter your key (integer): "))
                break
            except ValueError:
                print("Error: Key must be an integer.")
        encrypted_message = encryptC(message, key)  # присвоение переменной зашифрованного сообщения

    # Обработка неверного ввода ключа для Виженера
    elif cipher_type == 2:
        while True:
            key = input("Enter your key (letters only): ")
            if key.isalpha():  # проверка, что ключ состоит только из букв
                break
            else:
                print("Error: Key must contain letters only.")
        encrypted_message = encryptV(message, key)

    else:
        print("Error. Please, use valid cipher type.")
        return

    try:
        with open(path_write, 'w') as file:
            file.write(encrypted_message)
    except Exception as e:
        print(f"Error while saving the file: {e}")
        return

    print(f"Encryption completed successfully. Encrypted message saved to {path_write}.")

main()