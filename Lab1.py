# Натуральные числа. Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр.
# Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.

# словарь с прописными цифрами
digits = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

k = int(input('Введите число k: '))

numbers = []  # список с найденными в последовательности числами
work_buffer = ''
with open('data.txt') as input_file:
    buffer = input_file.read(1)
    while buffer:
        work_buffer = ''
        while buffer != ' ':
            work_buffer += buffer
            buffer = input_file.read(1)
            if not buffer:
                break
        buffer = input_file.read(1)

        output_data = ''
        cur_digit = ''  # текущая цифра пустая
        count = 0
        i = 0  # счетчик нужен для определения последняя цифра или нет

        for letter in work_buffer:
            if letter not in digits.keys() or work_buffer[0] == '0':
                break
            i += 1
            if cur_digit == '':  # если повторяющиеся цифры не считали
                count += 1  # увеличиваем счетчик
                cur_digit = letter  # повторяющаяся цифра = текущей
            else:  # если цифры уже находили
                if letter == cur_digit:  # если текущая цифра совпадает с повторяющейся
                    if i != len(work_buffer):  # и цифра не последняя
                        count += 1  # увеличиваем счетчик
                    else:  # если текущая цифра совпадает с повторяющейся и последняя
                        count += 1  # увеличиваем счетчик
                        if count > k:  # в последовательности больше k повторяющихся цифр?
                            output_data += work_buffer + f' {digits[cur_digit]} {count} '
                else:  # если текущая цифра не совпадает с повторяющейся
                    if count > k:  # найденных повторяющихся цифр больше k?
                        # если да, то записываем само число цифрами и прописью с количеством повторений
                        output_data += work_buffer + f' {digits[cur_digit]} {count} ' + '\n'
                    cur_digit = letter  # теперь искомая цифра - текущая
                    count = 1  # сбрасываем счетчик, т.к. это цифра и ее нужно тоже подсчитать, то начинаем с 1

        if output_data:
            print(output_data)
