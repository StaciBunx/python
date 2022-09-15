# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def convert_to_binary(number):
    '''
    Функция конвертирует число в десятичном представлении в список, состоящий из цифр остатка деления на 2.
    Затем переворачивает его и преобразовывает в тип int.
    Возвращает число в двоичном представлении
    '''
    number = int(number)
    binary_list = []
    binary_number = 0
    while number > 0:
        remainder_number = number % 2
        binary_list.append(remainder_number)
        number = int(number/2)
    binary_list.reverse()
    binary_number = int(''.join(map(str, binary_list)))
    return binary_number


print(convert_to_binary(45))
print(convert_to_binary(3))
print(convert_to_binary(2))
