# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.

def count_unique_characters(msg):
    low_msg = msg.lower()
    unique_chars = list(filter(lambda char: low_msg.count(char.lower()) <= 1, low_msg))
# Выводим уникальные символы (по желанию, можно удалить эту строку)
    print(unique_chars)
    return len(unique_chars)

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)