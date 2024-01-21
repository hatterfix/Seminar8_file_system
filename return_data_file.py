from choice_file import choice_number_file

# Исходник:

# def data_file():
#     nf = choice_number_file()
#     with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
#         data = file.readlines()
#     return data, nf

# Модифицировал, добавив возможножность передачи аргументов,
# для выбора номера файла при операции копирования
def data_file(file_number):
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf
