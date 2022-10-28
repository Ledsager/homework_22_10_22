# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


import random


def input_number(whose_move,igrok_1,igrok_2):
    if whose_move:
        print(f'ходит {igrok_1}')
    else:
        print(f'ходит {igrok_2}')
    

    while True:
        try:
            if not(whose_move) and igrok_2 == 'bot':
                hod_a=random.randint(0,28)
                print('bot забрал ',hod_a, ' конф.')
                return hod_a
                
            hod_a=int(input("Введите количество конфет которые забираете : "))
            if (hod_a < 1) or (hod_a > 28):
                print('количество конфет должно быть больше 0 и меньше 28, введите еще раз:')
            else:
                break
        except:
            print('Ошибка ввода, попробуйте еще раз')
    # print(hod_a)
    return hod_a


# igrok_1-true
# igrok_2-false

kol_konfet = 60
bot = int(input('Введите количество игроков (1 или 2): '))
if bot == 2:
    igrok_1 = 'igrok 1'
    igrok_2 = 'igrok 2'
else:
    igrok_1 = 'igrok 1'
    igrok_2 = 'bot'

whose_move = bool(random.getrandbits(1))


# print(whose_move)

while(kol_konfet > 0):
    if kol_konfet >= 29:
        kol_konfet = kol_konfet - input_number(whose_move,igrok_1,igrok_2)
        print(kol_konfet,' конф. осталось')
        whose_move = not(whose_move)
    else:
        whose_move = not(whose_move)
        break
    # print(kol_konfet , ' ' , whose_move)

if whose_move:
    print(f'Выиграл {igrok_2}')
else:
    print(f'Выиграл {igrok_1}')
