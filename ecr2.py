import string

ALPHABET = string.ascii_lowercase  # английский алфавит с маленькими буквами


#таблица для Виженера
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
            encrypted_position = (position + key) % len(ALPHABET) # % - деление с остатком. Если будет больше 26, перейдет на начало
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
        if message[i].lower() in ALPHABET:  # проверяем, является ли символ буквой
            pos_mes = ALPHABET.find(message[i].lower())
            pos_key = ALPHABET.find(full_key[key_index])
            encrypted_letter = VIGENERE_MATRIX[pos_mes][pos_key]
            #для заглавных:
            if message[i].isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_message += encrypted_letter  # добавляем зашифрованную букву
            key_index += 1
        else:
            encrypted_message += message[i]  # добавляем символы (пробелы) без изменений

    return encrypted_message

def main():
    print("Welcome to Ceaser & Vigenere encrypt program")
    cipher_type = int(input("Enter 1 if you want to use the Caesar's cipher or 2 to use the Vigenère's cipher: "))
    path_read = input("Enter path to your file: ")
    path_write = input("Enter save path to your file: ")
    if path_read == "": #если оставить поле ввода пустым, то автоматически сохранит в output и прочтет input
        path_read = "input.txt"
    if path_write == "":
        path_write = "output.txt"

    file = open(path_read, 'r')
    message = file.read()  # файл прочитается целиком
    file.close()

    if cipher_type == 1:
        key = int(input("Enter your key: "))
        encrypted_message = encryptC(message, key)#присвоили переменной зашифрованное сообщение
    elif cipher_type == 2:
        key = input("Enter your key: ")
        encrypted_message = encryptV(message, key)
    else:
        print("Error. Please, use valid cipher type.")
        exit()

    file = open(path_write, 'w')
    file.write(encrypted_message)
    file.close()# закрыли файл, чтобы освободить системный ресурс

main()

