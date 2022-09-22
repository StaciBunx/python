# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random


def get_candy_number():
    '''
    Функция проверяет число, которок пользователь вводит для суммы конфет в кучке. Возвращает модуль числа.
    '''
    while True:
        try:
            num = abs(int(input("Введите количество конфет в куче: ")))
            return num
        except ValueError:
            print("Вы ввели не число! Попробуйте еще раз.")


def get_pull_number_max():
    '''
    Функция проверяет число, которок пользователь вводит для макисмального значения. Возвращает модуль числа.
    '''
    while True:
        try:
            num = abs(
                int(input("Введите максимальное количество конфет в раунд, которое можно вытянуть: ")))
            return num
        except ValueError:
            print("Вы ввели не число! Попробуйте еще раз.")


def get_first_turn():
    '''
    Функция рандомно задает, кто будет первым ходить. Возвращает номер игрока.
    '''
    turn = 0
    turn = random.randint(1, 2)
    print(f"Ход начинает {turn} игрок.")
    return turn


def get_first_turn_wbot():
    '''
    Функция рандомно задает, кто будет первым ходить, в игре с компьюетром. Возвращает номер игрока.
    '''
    turn = 0
    turn = random.randint(1, 2)
    if turn == 1:
        print(f"Вы начинаете ход.")
    else:
        print(f"Ход начинает компьютер.")
    return turn


def turn_change(player_num):
    '''
    Функция переключает ходы между игроками, возвращает номер игрока.
    '''
    if player_num == 2:
        player_num = 1
    elif player_num == 1:
        player_num = 2
    return player_num


def game_pvp():
    '''
    Функция содержит в себе
    '''
    candy_qyt = get_candy_number()
    if candy_qyt == 0:
        print("В кучке нет конфет. Введите число больше нуля.")
        game_pvp()
    else:
        candy_pull_max = get_pull_number_max()
        if candy_pull_max > candy_qyt:
            print(
                "Нельзя вытянуть больше конфет, чем их количество в кучке. Введите число меньше!")
            game_pvp()
        elif candy_pull_max == 0:
            print(
                "Если ничего не вытягивать из кучки, то и поиграть не удастся. Введите число больше нуля.")
            game_pvp()
        else:
            print('-----------------')
            print("ИГРА НАЧИНАЕТСЯ")
            print('-----------------')
            current_player = get_first_turn()
            while candy_qyt > 0:
                num = int(input("Сколько вытянуть конфет: "))
                if num > candy_pull_max:
                    print(f"Нельзя брать больше {candy_pull_max} ")
                else:
                    print('-----------------')
                    candy_qyt -= num
                    print(f'В кучке {candy_qyt} конфет')
                    if candy_qyt == 0:
                        continue
                    current_player = turn_change(current_player)
                    print(f'Теперь ходит {current_player} игрок')

            print(f"Выиграл {turn_change(current_player)} игрок!")
            print('-----------------')
            print("КОНЕЦ ИГРЫ")
            print('-----------------')
            play_more_question = input("Хотите поиграть еще? (да/нет): ")
            if ((play_more_question.lower()) == 'да'):
                start_game()
            else:
                print("Хорошо, пока!")


def game_bot():
    candy_qyt = get_candy_number()
    if candy_qyt == 0:
        print("В кучке нет конфет. Введите число больше нуля.")
        game_bot()
    else:
        candy_pull_max = get_pull_number_max()
        if candy_pull_max > candy_qyt:
            print(
                "Нельзя вытянуть больше конфет, чем их количество в кучке. Введите число меньше!")
            game_bot()
        elif candy_pull_max == 0:
            print(
                "Если ничего не вытягивать из кучки, то и поиграть не удастся. Введите число больше нуля.")
            game_bot()
        else:
            print('-----------------')
            print("ИГРА НАЧИНАЕТСЯ")
            print('-----------------')
            current_player = get_first_turn_wbot()
            while candy_qyt > 0:
                if current_player == 1:
                    num = int(input("Сколько вытянуть конфет: "))
                    if num > candy_pull_max:
                        print(f"Нельзя брать больше {candy_pull_max} ")
                    else:
                        candy_qyt -= num
                        print(f'В кучке {candy_qyt} конфет')
                        if candy_qyt == 0:
                            continue
                        current_player = turn_change(current_player)
                        print(f'Переход хода.')
                if current_player == 2:
                    num = random.randint(1, candy_pull_max)
                    if num > candy_qyt:
                        num = random.randint(1, candy_qyt)
                    else:
                        print('-----------------')
                        print(f"Компьютер вытягивает {num} конфет.")
                        candy_qyt -= num
                        print(f'В кучке {candy_qyt} конфет')
                        print('-----------------')
                        if candy_qyt == 0:
                            continue
                        current_player = turn_change(current_player)
                        print(f'Переход хода.')
            if current_player == 1:
                print("Вы проиграли")
            else:
                print("Вы выиграли!")
            print('-----------------')
            print("КОНЕЦ ИГРЫ")
            print('-----------------')
            play_more_question = input("Хотите поиграть еще? (да/нет): ")
            if ((play_more_question.lower()) == 'да'):
                start_game()
            else:
                print("Хорошо, пока!")


def start_game():
    print('-----------------')
    print("ДОБРО ПОЖАЛОВАТЬ В ИГРУ CANDY CRUSH")
    print('-----------------')
    answer = input("Вы будете играть с человеком? (да/нет): ")
    if ((answer.lower()) == 'да'):
        print("Ок, усаживайтесь по-удобнее.")
        game_pvp()
    else:
        print("Тогда ваш оппонент - компьютер.")
        game_bot()


start_game()
