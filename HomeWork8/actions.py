import csv

def append_user(dict1):
    with open('D:\\Lena\\Geekbrains\\HomeWork\\HWPython\HomeWork8\DATABASE.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 1
        for row in reader:
            print(row)
            print(row['id'], type(row['id']))
            if max_id < int(row['id']):
                max_id = int(row['id'])
    print(max_id)

    dict1['id'] = str(max_id + 1)
    with open('D:\\Lena\\Geekbrains\\HomeWork\\HWPython\HomeWork8\DATABASE.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'last_name', 'first_name', 'second_name', 'phone_number','description']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writerow(dict1)

# with open('D:\\Lena\\Geekbrains\\HomeWork\\HWPython\HomeWork8\DATABASE.csv', 'r', encoding='utf-8') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=',')
#     for row in csv_reader:
#         print(row, ' - ', type(row))