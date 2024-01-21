from return_data_file import data_file

def copy_row():
    source_file = int(input("Введите номер файла, из которого хотите скопировать строку: "))
    target_file = int(input("Введите номер файла, в который хотите скопировать строку: "))

    source_data, source_nf = data_file(source_file)
    target_data, target_nf = data_file(target_file)

    row_number = int(input("Введите номер строки, которую необходимо скопировать: "))
    row_index = row_number - 1

    if row_index < 0 or row_index >= len(source_data):
        print("Ошибка! Введен неверный номер строки.")
        return

    row_to_copy = source_data[row_index]

    with open(f'db/data_{target_nf}.txt', 'a', encoding='utf-8') as target_file:
       target_file.write(row_to_copy + '\n')

    print("Строка успешно скопирована!")

