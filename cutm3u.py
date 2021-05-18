#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys

# имена файлов для работы
if len(sys.argv) > 1:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
else:
    print('Использование:')
    print('cutm3u.py file1.m3u file2.m3u')
    sys.exit(1)

# создадим массив строк для поиска
srchlist = ['group-title="ultra', 'group-title="фильмы', 'group-title="кино', 'group-title="спорт', 'group-title="познавательные', 'group-title="детские', 'group-title="мужские', 'group-title="россия']

# определим длинну массива строк переменных для поиска
listlength = len(srchlist)

# откроем файл f1
f1 = open(file1, encoding='utf8')

# читаем содержимое файла f1 в массив строк
linesf1 = f1.readlines()

# закроем файл f1
f1.close()

# определим длинну массива строк из файла f1
f1length = len(linesf1)

# формируем массив строк для записи в файл f2
linesf2 = []

# добавим заголовок в массив строк для записи в файл f2
linesf2.append(linesf1[0])

for i in range(f1length):
# читаем строку из массива строк файла f1
    s = linesf1[i]

# ...и преобразовываем её к нижнему регистру
    s = s.lower()

    for n in range(listlength):
        ss = srchlist[n]

# если в строке из массива строк файла f1 есть подстрока из массива для поиска,
        if ss in s:

# то добавим её и следующую строку в массив строк для записи в файл f2
            linesf2.append(linesf1[i])
            linesf2.append(linesf1[i+1])

# откроем файл f2
f2 = open(file2, 'w', encoding='utf8')

# сохраним подготовленный массив в файл f2
f2.writelines(linesf2)

# закроем файл f2
f2.close()
