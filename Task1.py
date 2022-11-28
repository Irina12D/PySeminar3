# Задача 1
'''
    Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
    Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

from random import randint
my_list = []
n = randint(5, 10)
for i in range(n):
    my_list.append(randint(1, 9))
sum = 0
for i in range(1, len(my_list), 2):
    sum += my_list[i]
print(*my_list)
print('сумма элементов списка с нечетными индексами равна', sum)