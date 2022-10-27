'''30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: 
ключи — ФИО, значения — данные о хобби.'''

# users1 = []
# hobby1 = []
# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/users.txt', 'r', encoding='utf-8') as users:
#       for line in users:
#         users1.append(line)
# str1 = users1
   
# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/hobby.txt', 'r', encoding='utf-8') as hobby:
#       for line1 in hobby:
#         hobby1.append(line1)
# str2 = hobby1      
# # print(str1,str2)
# info = dict(zip(str1,str2))
# # print(info)
# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/users_hobby.txt', 'w',encoding='utf-8') as out:
#     for key, val in info.items():
#         out.write('{}:{}'.format(key, val))
'''Проверка видимости файлов.У меня возникла проблема, что файлы txt не виделись python, поэтому пришлось прописывать весь путь'''
# import os
# # print (os.getcwd())
# print (os.listdir(os.getcwd()))

'''31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

# number = int(input('Введите натуральное число: '))

# def Multipliers(number):
#     multipliers = []
#     item = 2
#     while (item <= number):
#         if number % item == 0:
#             multipliers.append(item)
#             number = number/item
#         else:
#             item +=1    
#     return multipliers   

# print(f'Множители числа {number} = {Multipliers(number)} ')

'''32. Задайте последовательность чисел. Напишите программу,
 которая выведет список неповторяющихся элементов исходной последовательности.'''

# my_lists = ['1','5','2','1','45','8','2','45']
# print(f'Заданный список: {my_lists}')
# my_lists1 = []
# for i in my_lists:
#     if i not in my_lists1:
#         my_lists1.append(i)
# print(f'Список не повторяющихся элементов: {my_lists1}')    
   
# my_lists = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Заданный список: {my_lists}")
# new_lists = []
# [new_lists.append(i) for i in my_lists if i not in new_lists]
# print(f"Список из неповторяющихся элементов: {new_lists}")

'''33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0'''


# from random import randint

# k = int(input('Введите натуральную степень k:'))
# koeff=[randint(0,101) for i in range(k)]+[randint(1,101)]
# poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# # Поиск и замены:
# poly=poly.replace('x^1+', 'x+')
# poly=poly.replace('x^0', '')
# poly+=('','1')[poly[-1]=='+']
# poly=(poly, poly[:-2])[poly[-2:]=='^1']
# print(poly)


