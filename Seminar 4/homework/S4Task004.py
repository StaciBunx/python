# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


my_path = 'encrypt.txt'


def encrypt_message():
    '''Функция шифрует сообщение, введеное пользователем. Возвращает строку'''
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    input_string = input("Введите текст для шифрования: ")
    key = int(input("Введите ключ (от 1 до 32): "))
    encrypted = ""
    for letter in input_string:
        position = alphabet.find(letter.lower())
        new_position = position+key
        if letter.lower() in alphabet:
            encrypted += alphabet[new_position]
        else:
            encrypted += letter
    print(encrypted)
    return encrypted


def write_file(info, path):
    ''' Функция открывает файл (второй аргумент) и перезаписывает в него неоходимые данные (первый аргумент). Ничего не возвращает'''
    with open(path, 'w', encoding='utf-8') as file:
        file.write(info)


def read_file(path):
    '''Функция открывает и читает файл, возвращает строку из файла'''
    my_text = ''
    with open(path, 'r', encoding='utf-8') as file:
        my_text = file.read()
    return my_text


def decrypt_message(encrypted_text):
    '''Функция расшифровает сообщение(аргумент), просит пользователя ввести ключ. Возвращает расшифрованное сообщение в строке.'''
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    key = int(input("Введите ключ для дешифровки (от 1 до 32): "))
    decrypted = ""
    for letter in encrypted_text:
        position = alphabet.find(letter.lower())
        new_position = position-key
        if letter.lower() in alphabet:
            decrypted += alphabet[new_position]
        else:
            decrypted += letter
    print(decrypted)
    return decrypted


write_file(encrypt_message(), my_path)
decrypt_message(read_file(my_path))
