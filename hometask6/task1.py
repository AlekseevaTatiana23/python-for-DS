# Команде лингвистов понравилось качество ваших программ, поэтому они
# решили заказать функцию для анализатора текста, которая создавала бы
# список гласных букв в нём и считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует
# список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину.

# Запрашиваем у пользователя ввод текста
text = input('Введите текст: ')
# Создаём список гласных букв, которые есть в тексте
# Используем генератор списка для фильтрации гласных
vowels = [i for i in text if i in 'ауоыиэяюёе']
# Выводим список найденных гласных
print('Список гласных букв:', vowels)
# Выводим количество гласных в списке
print('Длина списка:', len(vowels))