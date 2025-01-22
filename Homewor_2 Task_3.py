import os


def read_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        read_data = file.read().strip()
        file_list = read_data.split('\n')
        count_row = sum(1 for line in open(file_name, encoding='utf-8'))
        return count_row, [read_data, file_name]


def process_file():
    content = {}
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            key, val = read_file(file_name)
            content[key] = val
    return content


def write_result(content):
    content_sorted = sorted(content.items())
    with open('123.txt', 'w', encoding='utf-8') as output_file:
        for key, val in content_sorted:
            output_file.write(f'{val[-1]}\n')
            output_file.write(f'{key}\n')
            output_file.write(f'{val[0]}\n')


content = process_file()
write_result(content)