# Задача 4
'''
    Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    Без применения встроенных методов (арифметически)
    Пример:
        45 -> 101101
        3 -> 11
        2 -> 10
'''

n = int(input("Введите целое число "))
n = abs(n)
result = ''
if n < 2:
    result = str(n)
else:
    result = ''
    while n > 0:
        result = str(n % 2) + result
        n //= 2
print(result)