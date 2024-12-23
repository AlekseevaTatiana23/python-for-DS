# Часто в программировании приходится писать код исходя из результата,
# который требует заказчик. В этот раз ему нужно получить двумерный список:
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# Напишите программу, которая генерирует такой список и выводит его на экран.
# Используйте только list comprehensions

# Создание двумерного списка с помощью list comprehension
# Внешний цикл по range(1, 5) определяет первый элемент каждой вложенной строки
# Внутренний цикл формирует элементы каждой строки с шагом 4

my_list = [[j_num for j_num in range(i_num, 13, 4)] for i_num in range(1, 5)]

print(my_list)
# Альтернативный вариант решения с использованием фиксированных смещений
second_answer = [[value, value + 4, value + 8] for value in range(1, 5)]
print(second_answer)
