#!/usr/bin/python3
#-*- coding: utf-8 -*-

# создадим массив строк для поиска
list = ['group-title="ultra', 'group-title="фильмы', 'group-title="кино', 'group-title="спорт', 'group-title="познавательные', 'group-title="детские', 'group-title="мужские', 'group-title="россия']

# откроем файлы
f1 = open('file1.m3u', encoding='utf8')
f2 = open('file2.m3u', 'w', encoding='utf8')

# читаем содержимое файла f1 в массив строк
lines = f1.readlines()

# определим длинну массива строк из файла f1
f1length = len(lines)

# определим длинну массива строк переменных для поиска
listlength = len(list)

# запишем заголовок из файла f1 в файл f2
f2.write(lines[0])

for i in range(f1length):
# читаем строку из файла f1
    s = lines[i]

# ...и преобразовываем её к нижнему регистру
    s = s.lower()

    for n in range(listlength):
        ss = list[n]

# если в строке из файла f1 есть подстрока из массива для поиска,
        if ss in s:

# то запишем её и следующую строку в файл f2
            f2.write(lines[i])
            f2.write(lines[i+1])

# закроем файлы
f2.close()
f1.close()	
