from datetime import datetime as dt
from user_interface import mode, type_numbers

def general(num1, num2, func, res, type_number):
   time = dt.now().strftime('%H:%M')
   with open ('log.txt', 'a', encoding='utf-8') as file:
       file.writelines(f'Время внесения данных {time}, Тип чисел : {type_numbers[type_number]}, Число первое : {num1}, Число второе : {num2}, Функция : {mode[func]}, Результат = {res} \n')