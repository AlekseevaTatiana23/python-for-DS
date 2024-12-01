# Напишите свою функцию sum, которая должна быть более гибкой, чем
# стандартная. Она должна уметь складывать числа:
# ● из списка списков,
# ● набора параметров.
# Основной код оставьте пустым или закомментированным (используйте его
# только для тестирования).

def my_sum(*args):
    total_sum = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum +=i_elem
        elif isinstance(i_elem, (list, tuple)):
            for x in i_elem:
                total_sum += my_sum(x)
    return total_sum

# Основной код для тестирования
#print(my_sum([[1, 2, [3]], [1], 3])) # Ожидаемый результат: 10
#print(my_sum(1, 2, 3, 4, 5)) # Ожидаемый результат: 15