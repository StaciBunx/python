from colorama import Fore


def check_float_number(number: str) -> float:
    '''
    Поверка дробного числа
    '''
    while True:
        try:
            return float(input(number))
        except ValueError:
            print(Fore.RED+f'Неверно! Должно быть дробное число!')


def check_symbol(symbol: str) -> str:
    '''
    Поверка знака действия
    '''
    while True:
        try:
            sym = input(symbol)
            if sym in '+ - * / **'.split():
                return sym
            raise ValueError
            #print(Fore.RED+f'Неверно! Должен быть знак действия ("+", "-", "*", "/","**")!')
        except ValueError:
            print(
                Fore.RED+f'Неверно! Должен быть знак действия ("+", "-", "*", "/","**")!')


def check_calc(digit: str) -> int:
    '''
    Поверка выбора калькулятора
    '''
    while True:
        try:
            calc_choice = int(input(digit))
            if calc_choice in [1, 2, 3]:
                return calc_choice
            raise ValueError
            #print(Fore.RED+f'Неверно! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных 2,для выхода 3')
        except ValueError:
            print(Fore.RED+f'Неверно! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных 2,для выхода 3')
