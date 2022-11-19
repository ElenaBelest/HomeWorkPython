'''1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) * Подумайте как наделить бота ""интеллектом""'''
# import random
# candies = int(input('Введите количество конфет: '))
# first_player = random.randint(1,2)

# print(f'Игру начинает Игрок номер {first_player} ')

'''Логику решения почти поняла, с какими то недочетами, но вот не могу все заключить в функции'''

# # def Player1(candies):
# #     player1 = int(input('Игрок 1, сколько конфет вы забираете? '))
# #     candies = candies - player1
# #     return print(f'Осталось {candies} конфет!')
    

# # def Player2(candies):
# #     player2 = int(input('Игрок 2, сколько конфет вы забираете? '))
# #     candies = candies - player2  
# #     return print(f'Осталось {candies} конфет!')
     

# # def play(candies):
# while candies > 1:
#         if first_player == 1:
#              player1 = int(input('Игрок 1, сколько конфет вы забираете, не больше 28 ? '))
#              candies = candies - player1
#              print(f'После хода Игрока 1 осталось {candies} конфет!')
#              player2 = int(input('Игрок 2, сколько конфет вы забираете, не больше 28? '))
#              candies = candies - player2  
#              print(f'После хода Игрока 2 осталось {candies} конфет!')  
#         #  print(Player1(candies),Player2(candies))
#         if first_player == 2:
#              player2 = int(input('Игрок 2, сколько конфет вы забираете, не больше 28? '))
#              candies = candies - player2  
#              print(f'После хода Игрока 2 осталось {candies} конфет!') 
#              player1 = int(input('Игрок 1, сколько конфет вы забираете, не больше 28? '))
#              candies = candies - player1
#              print(f'После хода Игрока 1 осталось {candies} конфет!')
            
#         #  print(Player2(candies),Player1(candies))
# else:
#     print(f'Поздравляю! Вы победили! Все конфеты Ваши!')

# # print(play(candies))

'''Игра с ботом'''

# while candies > 1:
#         if first_player == 1:
#              player1 = int(input('Игрок 1, сколько конфет вы забираете, не больше 28 ? '))
#              candies = candies - player1
#              print(f'После хода Игрока 1 осталось {candies} конфет!')
#              player2 = int(random.randint(1,29))
#              candies = candies - player2  
#              print(f'После хода Игрока 2 осталось {candies} конфет!')  
#         #  print(Player1(candies),Player2(candies))
#         if first_player == 2:
#              player2 = int(random.randint(1,29))
#              candies = candies - player2  
#              print(f'После хода Игрока 2 осталось {candies} конфет!') 
#              player1 = int(input('Игрок 1, сколько конфет вы забираете, не больше 28? '))
#              candies = candies - player1
#              print(f'После хода Игрока 1 осталось {candies} конфет!')
            
#         #  print(Player2(candies),Player1(candies))
# else:
#     print(f'Поздравляю! Вы победили! Все конфеты Ваши!')

# # print(play(candies))

'''3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''

# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork5/file_code1.txt', 'w') as data:
#     data.write('ggggggsssssssssssspppbbggggggggssssszzzzzzzzzzzzzzzzddd')


# def Encoded(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def Decoded(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork5/file_code1.txt', 'r') as file:
#     decoded_string = file.read()

# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork5/file_code.txt', 'w') as file:
#     encoded_string = Encoded(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + Encoded(decoded_string))
