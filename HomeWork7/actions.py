from calculations import sum,difference,div,multiplication
from user_interface import return_result


def act(num1, num2, action):
    if action == 1:
        result = sum(num1,num2)
    elif action == 2:
        result = difference(num1,num2)
    elif action == 3:
        result = multiplication(num1,num2)
    elif action == 4:
        result = div(num1,num2) 
    return result
