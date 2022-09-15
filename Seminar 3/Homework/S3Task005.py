# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)

def fibonacci(number):
    '''Функция создает последовательность до числа number, возвращает список'''
    fibonacci_list = []
    f1 = 1
    f2 = 1
    fibonacci_list.append(f1)
    fibonacci_list.append(f2)
    item = 2
    while item < number:
        f1, f2 = f2, f1+f2
        fibonacci_list.append(f2)
        item += 1
    return fibonacci_list


def fibonacci_nega(number):
    '''Функция создает последовательность нега Фибоначчи до числа number, возвращает список'''
    fibonacci_nega_list = []
    f1 = 1
    f2 = -1
    fibonacci_nega_list.append(f1)
    fibonacci_nega_list.append(f2)
    item = 2
    while item < number:
        f1, f2 = f2, f1-f2
        fibonacci_nega_list.append(f2)
        item += 1
    return fibonacci_nega_list


def join_fibonacci_lists(list, negalist):
    '''Функция переворачивает список с последовательностью нега, прибавляет ноль и склеивает с списком обычнм Фибоначчи. Возвращает итоговый список'''
    negalist.reverse()
    negalist.append(0)
    result_list = negalist+list
    return result_list


print(join_fibonacci_lists(fibonacci(8), fibonacci_nega(8)))
