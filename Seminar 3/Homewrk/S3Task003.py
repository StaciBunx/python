# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


from math import floor


def fractions_convert(my_list):
    '''Из заданного списка удаляет целочисленную часть, оставляя у элементов только дробную. Возвращает список c дробными значениями'''
    fraction_list = []
    i = 0
    while i < len(my_list):
        temp = floor(my_list[i])
        fraction = round((my_list[i] - temp), 10)
        fraction_list.append(fraction)
        i += 1
    return fraction_list


def fractions_diff(fraction_list):
    '''Считает разность между максимальным и минимальным значение, возвращает число'''
    result = round((max(fraction_list) - min(fraction_list)), 2)
    return result


print(fractions_diff(fractions_convert([1.1, 1.2, 3.1, 5.17, 10.02])))
print(fractions_diff(fractions_convert([4.07, 5.1, 8.2444, 6.98])))
