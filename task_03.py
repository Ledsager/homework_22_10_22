# Создайте программу для игры в ""Крестики-нолики"".

import random
import os


winer_xo = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]
 
# Вывод карты на экран

def print_maps(maps):

    for i in range(1, 10):
        if maps[i-1] == 'x':
            print("\033[31m\033[1m{}\033[0m" .format(maps[i-1]),' ',end = ' ')
        elif maps[i-1]=='o':
            print("\033[34m\033[1m{}\033[0m" .format(maps[i-1]),' ',end = ' ')
        else:
            print(maps[i-1], ' ', end = ' ')
        if i%3 == 0:
            print('\n')

def input_step(whose_move, igrok_1, igrok_2, maps):
    # print_maps(maps)
    if whose_move:
        print(f'ходит {igrok_1}')
    else:
        print(f'ходит {igrok_2}')
    while True:
        try:       
            hod_a = int(input("Введите ячейку : "))
            ind = maps.index(hod_a)
            # print(maps.index(hod_a),' ',maps[ind])
            if ((hod_a < 1) or (hod_a > 9))and((maps[ind] == 'o')or(maps[ind] == 'x')):
                print('введите не занятую ячейку введите еще раз:')
            else:
                break
        except:
            print('Ошибка ввода, попробуйте еще раз')
    if whose_move:
        maps[ind] = 'x'
        
    else:
        maps[ind] = 'o'
        
    # print(hod_a)
    return hod_a

def win_xo():
    win = ""
    for i in winer_xo:
        if maps[i[0]] == "x" and maps[i[1]] == "x" and maps[i[2]] == "x":
            win = "x"
        if maps[i[0]] == "o" and maps[i[1]] == "o" and maps[i[2]] == "o":
            win = "o" 
    return win
    
os.system('cls')
igrok_1 = 'igrok 1'
igrok_2 = 'igrok 2'
whose_move = bool(random.getrandbits(1))

maps=[i for i in range(1, 10)]
igra_go = True

# input_step(whose_move,igrok_1,igrok_2,maps)
# print_maps(maps)


while(igra_go):
    os.system('cls')
    print_maps(maps)
    input_step(whose_move,igrok_1,igrok_2,maps)

    if win_xo() == "x" or win_xo() == "o":
        igra_go = False
    else:
        whose_move = not(whose_move)

if whose_move:
    print_maps(maps)
    print("\033[31m\033[1m{}\033[0m Выиграл " .format(igrok_1))
else:
    print_maps(maps)
    print("\033[34m\033[1m{}\033[0m Выиграл " .format(igrok_2))
