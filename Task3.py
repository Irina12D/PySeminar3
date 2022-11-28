# Задача 3
'''
    Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
    Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

import random
my_list = []
n = random.randint(5, 10)
for i in range(n):
    precision = random.randint(0, 4)
    value = round(random.uniform(1, 20), precision)
    if precision == 0 or precision == 1 and value*10 % 10 == 0:
        value = int(value)
    my_list.append(value)
print(*my_list)

max_value = 0
min_value = 10**12
for i in my_list:
    if i == int(i):
        continue
    s = str(i).split('.')
    dr = float('0.' + s[1])
    if dr > max_value: max_value = dr
    if dr < min_value: min_value = dr
if max_value == 0:
    print("все числа оказались целыми")
else:
    print("минимальное значением дробной части элементов равно", min_value)
    print("максимальное значением дробной части элементов", max_value)
    print("разница равна", max_value-min_value)