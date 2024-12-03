# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
# заменялась на следующую по алфавиту через K позиций по кругу. Если взять
# русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
# буква А станет буквой Г, Б станет Д и так далее.
# Пользователь вводит сообщение и значение сдвига. Напишите программу,
# которая изменит фразу при помощи шифра Цезаря.

# Определение русского алфавита, включая букву 'ё'
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# Функция для шифрования текста по методу Цезаря
def caesar_cipher(string, user_shift):
# Создание списка зашифрованных символов
    char_list = [(alphabet[(alphabet.index(symbol) + user_shift) % len(alphabet)]
                if symbol in alphabet else symbol)
                for symbol in string]
# Преобразование списка символов в строку
    new_str = ''.join(char_list)
    return new_str

# Ввод пользователем исходного сообщения и сдвига
input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

# Шифрование сообщения
output_str = caesar_cipher(input_str, shift)
# Вывод зашифрованного сообщения
print('Зашифрованное сообщение:', output_str)