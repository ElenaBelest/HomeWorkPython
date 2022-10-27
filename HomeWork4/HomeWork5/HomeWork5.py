'''1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) * Подумайте как наделить бота ""интеллектом""'''
import random
candies = int(input('Введите количество конфет: '))
first_player = random.randint(1,2)

print(f'Игру начинает Игрок номер {first_player} ')

# def Player1(candies):
#     player1 = int(input('Игрок 1, сколько конфет вы забираете? '))
#     candies = candies - player1
#     return print(f'Осталось {candies} конфет!')
    

# def Player2(candies):
#     player2 = int(input('Игрок 2, сколько конфет вы забираете? '))
#     candies = candies - player2  
#     return print(f'Осталось {candies} конфет!')
     

# def play(candies):
while candies > 1:
        if first_player == 1:
             player1 = int(input('Игрок 1, сколько конфет вы забираете, не больше 28 ? '))
             candies = candies - player1
             print(f'После хода Игрока 1 осталось {candies} конфет!')
             player2 = int(input('Игрок 2, сколько конфет вы забираете, не больше 28? '))
             candies = candies - player2  
             print(f'После хода Игрока 2 осталось {candies} конфет!')  
        #  print(Player1(candies),Player2(candies))
        if first_player == 2:
             player2 = int(input('Игрок 2, сколько конфет вы забираете, не больше 28? '))
             candies = candies - player2  
             print(f'После хода Игрока 2 осталось {candies} конфет!') 
             player1 = int(input('Игрок 1, сколько конфет вы забираете, не больше 28? '))
             candies = candies - player1
             print(f'После хода Игрока 1 осталось {candies} конфет!')
            
        #  print(Player2(candies),Player1(candies))
else:
    print(f'Поздравляю! Вы победили! Все конфеты Ваши!')

# print(play(candies))