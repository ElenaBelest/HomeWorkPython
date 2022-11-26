
from actions import *
from user_interface import *
from logger import general

def start():
    act = get_action()
    if act == 2:
        temp_dict = get_value_mod_2()
        append_user(temp_dict)
        general(act)