import csv

def get_action():
    mode = int(input('Введите число соответствующее вашему действию \
        1 - Просмотр данных абонента по Фамилии \
        2 - Добавление нового абонента \
        3 - Удаление абонента \
        4 - Перезапись данных абонента '))
    return mode
    
action = {1:'Просмотр данных абонента по Фамилии', 2: 'Добавление нового абонента', 3: 'Удаление абонента', 4: 'Перезапись данных абонента ' }


def get_value_mode():
    return input('Введите данные: ')

fieldnames = ['id', 'last_name', 'first_name', 'second_name', 'phone_number','description']    

def get_value_mod_2():
  fieldnames = ['id', 'last_name', 'first_name', 'second_name', 'phone_number','description']
  dict_data = {}
  for el in fieldnames:
    dict_data[el] = input(f'Введите {el} ')
  dict_data['id'] = int(dict_data['id'])
  return dict_data