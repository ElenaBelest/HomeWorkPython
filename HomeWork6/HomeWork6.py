'''14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11'''

# n = input('Введите вещественное число: ')
# sum = sum(map(int, n.replace('.', '')))
# print (sum)


'''2. Напишите программу, которая найдёт произведение пар чисел списка.
 Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

# import math
# list_a = list(map(int, input('Введите числа, через пробел: ').split()))
# print('Исходный список: ',list_a)
# print('Результат: ',list([a*b for a,b in zip(list_a[0:math.ceil(len(list_a)/2)],list_a[::-1])]))

'''18. *Реализуйте алгоритм перемешивания списка.'''

# import random

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Исходный список:  {list}')
# random.shuffle(list)
# print(f'Перемешанный список: {list}')

'''4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

# print(f'{int(input()):b}')

'''15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
 Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

# n = int(input('Enter number: '))
# factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
# print(factorial(n))
