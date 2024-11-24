#Дана последовательность из N целых чисел и число
#K. Необходимо сдвинуть всю последовательность
#(сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]

my_list = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(my_list)

list_res = []
for i in range(k):
    list_res.append(my_list[len(my_list - 1 - i)])
print(list_res)

for i in range(len(my_list) - k):
    list_res.append(my_list[i])
print(list_res)
