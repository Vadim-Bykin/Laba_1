# Натуральные числа. Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр.
# Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.

k = int(input('Введите K: '))
vocabulary = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
buffer_len = 1 # размер буфера чтения
work_buffer_len = buffer_len # длина рабочего буфера
work_buffer = '' # рабочий буфер
count = 0 # количество подряд идущих одинаковых цифр
num = [] # полный список чисел из файла
a = [] # список чисел, которые будут подходить под условие задачи

with open('text.txt', 'r') as text:
    buffer = text.read(buffer_len) # читаем первый блок
    if not buffer:
        print('Выбранный файл пустой.')
    while buffer: # обрабатываем текущий блок
        while buffer >= '0' and buffer <= '9':
            work_buffer += buffer
            buffer = text.read(buffer_len)
        if work_buffer:
            num.append(int(work_buffer))
            for item in range(1, len(work_buffer)):
                if work_buffer[item] == work_buffer[item - 1]:
                    count += 1
            if count > k:
                a.append(int(work_buffer))
        work_buffer = ''
        buffer = text.read(buffer_len)

if len(num) == 0:
    print('В файле нет подходящих под условие чисел')
    quit()

print('Иходный список чисел: ', num)
print('Список чисел, подходящих под условия: ', a)