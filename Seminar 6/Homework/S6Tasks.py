# **Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

from math import sqrt

# 1 - Определить, присутствует ли в заданном списке строк, некоторое число


def result(list):
    return 'Число присутствует' if list else 'Число отсутствует'

checked_list = ' '.join(map(
    str, [word for word in ['saf4', 'aghh', 'dfh6', 'dsah', 'sxY4'] if '4' in word]))
print(result(checked_list))

# 2 - Найти сумму чисел списка стоящих на нечетной позиции

data = [x for x in range(1, 10)]
res = sum(data[::2])
print(f'Сумма чисел списка, стоящих на нечетных позициях: {res}')

# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

input_points = input(
    'Введите коордианты для двух точек через пробел (4 цифры): ')
points = [int(x) for x in input_points.split(' ')]
print(
    f'Расстояние между точками равно {round((sqrt(int((points[2]- points[0]))**2+int((points[1] - points[3]))**2)), 2)}')

# 4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def search_repeat(my_list, my_string):
    try:
        second_appear = [x for x in range(len(my_list))[my_list.index(
            my_string)+1::] if my_list[x] == my_string]
        if second_appear:
            print(f'Позиция второго вхождения: {second_appear[0]}')
        else:
            print('-1')
    except ValueError:
        # Насколько я понимаю, то -1 - означает, что элемента в списке нет (как в примерах)
        print('-1')


search_repeat(["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe")
search_repeat(["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу")
search_repeat(["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу")
search_repeat(["123", "234", 123, "567"], "123")
search_repeat([], "123")

# 5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multi_pairs(my_list):
    half = len(my_list)//2 + len(my_list) % 2
    list_result = [my_list[x] * my_list[-1-x] for x in range(0, half)]
    print(list_result)


multi_pairs([2, 3, 4, 5, 6])
multi_pairs([2, 3, 5, 6])


# 6 - Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

result = [(-3) ** i for i in range(5)]
print(result)
