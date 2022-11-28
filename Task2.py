# Задача 2
'''
    Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    Пример:
        [2, 3, 4, 5, 6] => [12, 15, 16];
        [2, 3, 5, 6] => [12, 15]
'''

from random import randint
my_list = []
n = randint(5, 10)
for i in range(n):
    my_list.append(randint(1, 9))
product = []
count_pairs = len(my_list)//2
if n % 2 != 0:
    count_pairs += 1
for i in range(count_pairs):
    product.append(my_list[i] * my_list[len(my_list) - 1-i])
print('Исходный список:', *my_list)
print(f'Произведение пар:', *product)