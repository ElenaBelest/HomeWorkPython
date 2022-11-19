def get_value():
  value_1 = int(input('Enter first number : '))
  value_2 = int(input('Enter second number : '))
  return value_1, value_2

def get_type():
    type = input('Enter type of numbers (enter 1 - natural number, enter 2 - complex number, enter 3 - rational number): ')
    if type.lower() == '1':
        return 1 
    elif type.lower() == '2':
        return 2
    elif type.lower() == '3':
        return 3
    else:
        print('Error! Enter the correct number! ')              

type_numbers = {1 : 'natural number', 2 : 'complex number', 3 : 'rational number'}

def get_mode():
  mode = input('Enter the operation (+, -, * , /): ')
  if mode.lower() == '+':
    return 1
  elif mode.lower() == '-':
    return 2
  elif mode.lower() == '*':
    return 3
  elif mode.lower() == '/':
    return 4    
  else:
    print('Error! Enter the correct operation!')

mode = {1: 'sum', 2: 'difference', 3: 'multiplication', 4: 'dividing'}

def return_result(res, oper):
    return f'The result of the {mode[oper]}  of two numbers = {res}'  

from fractions import Fraction
from math import *        

def get_complex_num():
    value_1 = int(input('Enter the actual part of the first number: '))
    value_2 = int(input('Enter the imaginary part of the first number: '))
    value_3 = int(input('Enter the actual part of the second number: '))
    value_4 = int(input('Enter the imaginary part of the second number: '))
    num1 = complex(value_1, value_2)
    num2 = complex(value_3, value_4)
    return num1, num2

def get_rational_num():
    value_1 = float(input('Enter the first number in the fraction format (1.23 or -23.5): '))
    value_2 = float(input('Enter the second number in the fraction format (1.23 or -23.5): '))
    num1 = Fraction(value_1)
    num2 = Fraction(value_2)
    return num1, num2
