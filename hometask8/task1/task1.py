# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt.

import os


number_file = open('numbers.txt', 'r', encoding='utf-8')
total_sum = 0
for line in number_file:
# Разбиваем строку на части, используя пробелы и новые строки в качестве разделителей
# Преобразуем каждую часть в целое число и накапливаем сумму
    numbers = [int(num) for num in line.split() if num]
    total_sum += sum(numbers)

# Закрываем файл после чтения
number_file.close()

# Открываем выходной файл для записи
sum_file = open("answer.txt", "w", encoding="utf-8")
# Записываем сумму в выходной файл
sum_file.write(str(total_sum))
# Закрываем выходной файл
sum_file.close()