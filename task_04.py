# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode_f(s):

    encoding_str = ""
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        # добавляет к результату текущий символ и его количество

        encoding_str += str(count) + s[i]
        i = i + 1

    return encoding_str


def decode_f(c):

    decoding, number_symbol = "", ""
    i = 0
    while i < len(c):
        # формирует строку пока текущий символ число 
        if c[i].isdigit():
            number_symbol += c[i]
            i += 1
        else:
            # если очередной символ не число , преобразуем строку полученую выше(number_symbol) в число
            # и выводим текущий символ number_symbol раз
        
            decoding += c[i]*int(number_symbol)
            number_symbol = ""
            i += 1

    return decoding


def file_code(file_start, finish_file, function_coder):

    with open(file_start, 'r', encoding='utf-8') as file1:
        while True:
            string_file1 = file1.readline()
            if string_file1 == '':
                print('End Of File')
                break
            with open(finish_file, 'w', encoding='utf-8') as file2:
                file2.write(encode_f(string_file1))


def file_decode(file_start, finish_file, function_coder):

    with open(file_start, 'r', encoding='utf-8') as file1:
        while True:
            string_file1 = file1.readline()
            if string_file1 == '':
                print('End Of File')
                break
            with open(finish_file, 'w', encoding='utf-8') as file2:
                file2.write(decode_f(string_file1))


filename1 = "encode.txt"
filename2 = "decode.txt"
filename = "start.txt"

file_code(filename, filename1, 3)
file_decode(filename1, filename2, 3)

