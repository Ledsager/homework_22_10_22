# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


filename1 = "text.txt"
filename2 = "text-finish.txt"
# find_txt = 'абв'

find_txt=input('Введите буквы (слова с этими буквами будут удалены): ')
with open(filename1, 'r', encoding='utf-8') as file1:
    while True:
        string_file1 = file1.readline()
        if string_file1 == '':
            print('End Of File')
            break
        lst_file1 = [i for i in string_file1.split() if find_txt not in i]
        print(lst_file1)
        lst_file2 = ' '.join(lst_file1)
        with open(filename2, 'a', encoding='utf-8') as file2:
            file2.write(lst_file2 + '\n')
       