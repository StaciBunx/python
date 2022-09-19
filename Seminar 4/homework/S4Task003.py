# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4


file_path = 'students.txt'


def read_file(path):
    '''Функция открывает и читает файл, возвращает строковый список записей из этого файла'''
    students_list = []
    with open(path, 'r', encoding='utf-8') as students:
        for line in students:
            students_list.append(line)
    return students_list


def uppercase_for_5(students_list):
    ''' Функция определяет, если в элементе списка содержится оценка 5, то буквы этого элемента делает заглавными, возвращает список с заглавными буквами'''
    # К сожалению, не получалось перезаписать список, фукнкция почему-то возвращала все-равно со строчными, поэтому пришлось создавать новый список и в него уже передавать данные.
    upper_list = []
    for record in students_list:
        if '5' in record:
            record = record.upper()
            upper_list.append(record)
        else:
            upper_list.append(record)
    return upper_list


def write_file(info, path):
    ''' Функция открывает файл (второй аргумент) и перезаписывает в него неоходимые данные (первый аргумент). Ничего не возвращает'''
    with open(path, 'w', encoding='utf-8') as students:
        for record in info:
            students.write(record)


write_file(uppercase_for_5(read_file(file_path)), file_path)
