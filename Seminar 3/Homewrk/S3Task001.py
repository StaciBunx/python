# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def uneven_index_sum(my_list):
    '''Суммирует значения на нечетных позициях (без учета индекса 0), возвращает сумму'''
    result = 0
    result = sum(my_list[1::2])
    return result


print(uneven_index_sum([2, 3, 5, 9, 3]))
