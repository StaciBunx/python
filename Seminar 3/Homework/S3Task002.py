# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multi_index(my_list):
    '''Переумножает парные индексы с разных концов списка, возвращает новый список с произведением значений'''
    result_list = []
    list_half = len(my_list)/2
    i = 0
    temp = 0
    while i < list_half:
        temp = my_list[i]*my_list[len(my_list)-i-1]
        result_list.append(temp)
        i += 1
    return result_list


print(multi_index([2, 3, 4, 5, 6]))
print(multi_index([2, 3, 5, 6]))
