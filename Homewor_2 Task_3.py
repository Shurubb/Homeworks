file_1 = '1.txt'
file_2 = '2.txt'
file_3 = '3.txt'


with open(file_1, encoding='utf-8') as file:
    read_1 = file.read().strip()
    file_list_1 = read_1.split('\n')
    count_row_1 = sum(1 for line in open(file_1, encoding='utf-8'))


with open(file_2, encoding='utf-8') as file:
    read_2 = file.read().strip()
    file_list_2 = read_2.split('\n')
    count_row_2 = sum(1 for line in open(file_2, encoding='utf-8'))


with open(file_3, encoding='utf-8') as file:
    read_3 = file.read().strip()
    file_list_3 = read_3.split('\n')
    count_row_3 = sum(1 for line in open(file_3, encoding='utf-8'))
content = {
    count_row_1: [read_1, file_1],
    count_row_2: [read_2, file_2],
    count_row_3: [read_3, file_3],
}


content_sorted = sorted(content.items())


with open('123.txt', 'w', encoding='utf-8') as file:
    for key, val in content_sorted:
        write = file.write(f'{str(val[-1])}\n')
        write = file.write(f'{key}\n')
        write = file.write(f'{str(val[0])}\n')