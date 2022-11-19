
from actions import act
from user_interface import  *
from logger import general


def launch_rocket():
    type_number =  get_type()
    if type_number == 1:
        num1, num2 = get_value()
        action = get_mode()
        result = act(num1, num2, action)
        print(return_result(result, action))  
        general(num1, num2, action, result, type_number)
    elif type_number == 2: 
        num1, num2 = get_complex_num()
        action = get_mode()
        result = act(num1, num2,action)
        print(return_result(result, action))  
        general(num1, num2, action, result, type_number)
    elif type_number == 3:
        num1, num2 = get_rational_num()
        action = get_mode()
        result = act(num1, num2, action)
        print(return_result(result, action))  
        general(num1, num2, action, result, type_number)
    else:
        print('Error!')    
        
               