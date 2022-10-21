with open('tests.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        print(line)
    print(file_1.closed)
print(file_1.closed)