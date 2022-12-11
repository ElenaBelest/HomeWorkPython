
from actions import *
from user_interface import *
from logger import general
from write_new_base import *

def start():
    act = get_action()
    if act == 0:
        temp_dict = get_info()
        append_user(temp_dict)
        general(act)
    elif act == 2:
        temp_dict = get_value_mod_2()
        append_user(temp_dict)
        general(act)