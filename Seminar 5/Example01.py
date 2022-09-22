# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени n.

# *Пример:*

# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
my_path = r'C:\Users\79055\Desktop\Семинары\Python\Seminar 5\polinom.txt'


def get_number(input_string):
    ''' Получение числа '''
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print('Введите число')


def write_file(polinomial):
    '''Запись многочлена в файл'''
    f = open(my_path, 'a', encoding='utf-8')
    f.write(polinomial)
    f.close()


n = abs(get_number('Введите натуральную степень: '))

polinom = ''

for i in range(n, -1, -1):
    a = random.randint(0, 100)
    if a == 1:
        polinom += 'x**'+str(i)+'+'
    if a > 1 and i != 0 and i != 1:
        polinom += str(a)+'*x**'+str(i)+'+'
    if i == 1:
        polinom += str(a)+'*x+'
    if i == 0:
        polinom += str(a)+'=0' + '\n'

print(polinom)
write_file(polinom)
