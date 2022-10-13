# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Enter number: ')

def SumNumbers(number):
    sum = 0
    for i in number:
     if i != '.':
        sum += int(i)
    return sum


print(f'The sum of the digits of the number  {number} is {SumNumbers(number)} ')