# 2. Задайте два числа. Напишите программу, которая найдет НОК
#  (наименьшее общее кратное) этих двух чисел.
#  НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
nok = max(num_1, num_2)
while True:
    if nok % num_1 == 0 and nok % num_2 == 0:
        print("НОК", nok)
        break
    else:
        nok += 1
