# Одна библиотека поручила вам написать программу для оцифровки словарей
# синонимов. На вход в программу подаётся N пар слов. Каждое слово является
# синонимом для своего парного слова.
# Реализуйте код, который составляет словарь синонимов (все слова в словаре
# различны), затем запрашивает у пользователя слово и выводит на экран его
# синоним. Обеспечьте контроль ввода: если такого слова нет, выведите ошибку
# и запросите слово ещё раз. При этом проверка не должна зависеть от регистра
# символов.

synonims_dict = {}

num_pairs = int(input('Введите количество пар синонимов: '))

for i_pair in range(num_pairs):
    first_word, second_word = input(f'{i_pair + 1} пара: ').lower().split(' - ')
    synonims_dict[first_word] = second_word
    synonims_dict[second_word] = first_word

# Запускаем бесконечный цикл для ввода слова и поиска синонима
while True:
# Запрашиваем слово у пользователя и приводим его к нижнемурегистру
    word = input('Введите слово: ').lower()
    if word in synonims_dict:
        print(synonims_dict[word].capitalize())
        break
    else:
        print('Такого слова в словаре нет! ')
