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


def decode(c):

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
        
            decoding = c[i]*int(number_symbol)
            number_symbol = ""
            i += 1

    return decoding

decode('1s2d2d2d2d2f')