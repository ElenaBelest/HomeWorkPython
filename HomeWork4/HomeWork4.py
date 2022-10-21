'''30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: 
ключи — ФИО, значения — данные о хобби.'''

users1 = []
hobby1 = []
with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/users.txt', 'r', encoding='utf-8') as users:
      for line in users:
        users1.append(line)
str1 = users1
   
with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/hobby.txt', 'r', encoding='utf-8') as hobby:
      for line1 in hobby:
        hobby1.append(line1)
str2 = hobby1      
# print(str1,str2)
info = dict(zip(str1,str2))
# print(info)

# with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/users_hobby.txt', 'w',encoding='utf-8') as out:
#     out.writelines(info)


with open('D:/Lena/Geekbrains/HomeWork/HWPython/HomeWork4/users_hobby.txt', 'w',encoding='utf-8') as out:
    for key, val in info.items():
        out.write('{}:{}\n'.format(key, val))
'''Проверка видимости файлов'''
# import os
# # print (os.getcwd())
# print (os.listdir(os.getcwd()))