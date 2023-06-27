
print('***************Задача №1***************')
import random

# читаем текст из файлов
names_file = open('names.txt', 'r', encoding='utf-8')
cities_file = open('cities.txt', 'r', encoding='utf-8')
auto_file = open('auto.txt', 'r', encoding='utf-8')
names = names_file.read()
cities = cities_file.read()
auto = auto_file.read()
names_file.close()
cities_file.close()
auto_file.close()

# убираем переносы строк, преобразуем в массивы
names = names.replace('\n', ' ').split()
cities = cities.replace('\n', ' ').split()
auto = auto.replace('\n', ' ').split()

# перемешиваем массивы в случайном порядке
random.shuffle(names)
random.shuffle(cities)
random.shuffle(auto)

# собираем массивы в зип
text = list(zip(names, cities, auto))

# кортежи в массивы
text = list(map(lambda x: list(x), text))

# формируем массив текстов
text = list(map(lambda x: x[0] + ' живёт в городе ' + x[1] + ' и ездит на ' + x[2], text))

# преобразуем массив текстов в строку
text = '\n'.join(text)

print(text)

# записываем результат в файл
result_file = open('result.txt', 'w', encoding='utf-8')
result_file.write(text)
result_file.close()



print('\n\n***************Задача №2***************')
import re

# читаем текст из файла
albert_file = open('albert.txt', 'r', encoding='utf-8')
text = albert_file.read()
albert_file.close()

# выбрасываем знаки препинания, заменяем пробелами
text = re.sub('[\.\,\(\)\—\-]', ' ', text).split()


# выбираем только слова длиннее 7 символов
text7 = list(filter(lambda x: len(x) > 7, text))
einstein = open('einstein.txt', 'w', encoding='utf-8')
einstein.write(' '.join(text7))
einstein.close()


# выводим на экран слова длиннее 7 символов по n в строке
a = 0
n = 7
for i in range(len(text7) // n + 1):
    print(' '.join(text7[a:a + n]))
    a += n

