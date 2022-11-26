# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = input('Enter number: ')

# def SumNumbers(number):
#     sum = 0
#     for i in number:
#      if i != '.':
#         sum += int(i)
#     return sum


# print(f'The sum of the digits of the number  {number} is {SumNumbers(number)} ')

# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Enter number: '))
prodact = 1

for i in range(1,number+1):
    prodact *= i
    print(prodact, end=' ')
    
#  16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

# number = int(input('Введите число: '))
# my_list = {}

# def MyList(number):
   
#     for i in range (1,number+1):
#         my_list[i] = round((1+1/i)**i, 2)
#     return my_list  

# print(f'Cписок из {number} чисел последовательности (1+1/{number})^{number} = {MyList(number)} ')    

# my_list2 = [round((1+1/i)**i, 3) for i in range(1, number+1)] 

# print(f'Сумма последовательности чисел = {round(sum(my_list2), 2)} ')

# # запись решения (my_list2)нашла в интернете, так как не поняла почему 
# #не сработл метод аналогичный MyList(number) c задаванием my_listу вид не словаря а массива (my_list = [])
# #my_list2 = []
# #def MyList2(number):
   
#     # for i in range (1,number+1):
#     #     my_list2[i] = (1+1/i)**i
#     # return my_list2  



# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на введенных пользователем позициях.

# n = int(input('Ведите число '))
# count = n*2
# index1 = int(input(f'Ведите номер первого элемента от 0 до {count} : '))
# index2 = int(input(f'Ведите номер второго элемента от 0 до {count} : '))

# listN = []

# def Lists(n):
#     for i in range(-n,n+1):
#       listN.append(i)
#     return listN  
        
# print(f'Список чисел {Lists(n)} ')  

# n1 = listN[index1]
# n2 = listN[index2]

# index1 = listN[index1]
# index2 = listN[index2]

# prd = index1*index2

# print(f'Произведение чисел {n1} и {n2} равно {prd} ')


# 18. *Реализуйте алгоритм перемешивания списка.


# import random

# lists1 = ['apple','oranges','cherry','10','2022']
# print(f'Изначальный список {lists1} ')
# lenght = len(lists1)
# for i in range(lenght):
#     j = random.randint(0,lenght - 1)
#     temp = lists1[i]
#     lists1[i] = lists1[j]
#     lists1[j] = temp

# print(f'Перемешаный список: {lists1}')

