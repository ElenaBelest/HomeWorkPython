# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# number = int(input('Enter number from 1 to 7: '))
# if number == 1:
#     print('No')
# elif number == 2:
#     print('No')    
# elif number == 3:
#     print('No')    
# elif number == 4:
#     print('No')    
# elif number == 5:
#     print('No')    
# elif number == 6:
#     print('Yes')    
# elif number == 7:
#     print('Yes')    
# elif number > 7:
#     print('Bad number')   

# 8. Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# x = int(input('Enter first number  '))
# y = int(input('Enter first number  '))
# if x > 0 and y > 0:
#     print('1')
# if x < 0 and y > 0:
#     print('2')
# if x < 0 and y < 0:
#     print('3')
# if x > 0 and y < 0:
#     print('4')

# 9. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# number = int(input('Enter number from 1 to 4 '))
# if number == 1:
#     print('x > 0 and y > 0')
# elif number == 2:
#     print('x < 0 and y > 0')
# elif number == 3:
#     print('x < 0 and y < 0')
# elif number == 4:
#     print('x > 0 and y < 0')    
# elif number > 4:
#      print('Bad number') 

# 10. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# print('Enter coordinates point А:')
# xA = float(input('X: '))
# yA = float(input('Y: '))
# print("Enter coordinates point B:")
# xB = float(input('X: '))
# yB = float(input('Y: '))
# distance = round(((xB - xA)**2 + (yB - yA)**2)**(1 / 2), 2)
# print(f'Distance between points:  {distance} ')

