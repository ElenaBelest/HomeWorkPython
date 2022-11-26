from datetime import datetime as dt
from user_interface import action


def general(func):
   time = dt.now().strftime('%H:%M')
   with open ('D:\\Lena\\Geekbrains\\HomeWork\\HWPython\\HomeWork8\\logbase.txt', 'a', encoding='utf-8') as file:
       file.writelines(f'Время внесения данных {time}, какая операция совершена {action[func]} \n')