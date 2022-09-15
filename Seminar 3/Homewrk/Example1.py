# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

from typing import List


def have_number(list_number, number):
    have_number = False
    for word in list_number:
        for elem in word:
            if (elem == str(number)):
                have_number = True
                print(f'Такой элемент есть')
                break
    if have_number == False:
        print('Такого элемента нет')


have_number(['gwr5', 'sdGSDH', '8', 'sdHH'], 5)
