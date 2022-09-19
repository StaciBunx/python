# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

input_path = 'rle_input.txt'
output_path = 'rle_output.txt'


def read_file(path):
    '''Функция открывает и читает файл, возвращает строку из файла'''
    my_text = ''
    with open(path, 'r', encoding='utf-8') as file:
        my_text = file.read()
    return my_text


def rle_encode(data):
    '''Функция производит кодирование RLE, возвращает сжатую строку'''
    my_message = ''
    if data == '':
        return ''
    encoded = []
    count = 1
    for index in range(1, len(data)):
        if data[index] == data[index-1]:
            count += 1
        else:
            encoded.extend([str(count), str(data[index-1])])
            count = 1
    encoded.extend([str(count), str(data[index-1])])
    my_message = str(''.join(encoded))
    return my_message


def write_file(info, path):
    ''' Функция открывает файл (второй аргумент) и перезаписывает в него неоходимые данные (первый аргумент). Ничего не возвращает'''
    with open(path, 'w', encoding='utf-8') as file:
        file.write(info)


write_file(rle_encode(read_file(input_path)), output_path)
