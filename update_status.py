# Заметка
dict_note = {
'username': 'Алексей',
'content': 'Д.З.2',
'status': 'В процессе',
'reated_date': '27.01.2025',
'issue_date': '03.02.2025',
'title': ['Заголовок 1', 'Заголовок 2', 'Заголовок 3']
}
# Статусы заметки (Словарь)
dict_status = {
1: 'В процессе',
2: 'Отложено',
3: 'Выполнено'
}

len_dict_status = len(dict_status) # количество стаутсов в первоначальной заметке
# Текущий статус заметки
print('Заметка в текущем статусе: \n'
    f'Имя пользователя - {dict_note['username']} \n' 
    f'Описание заметки - {dict_note['content']} \n'
    f'Статус заметки - {dict_note['status']} \n'
    f'Дата создания: {dict_note['reated_date']} \n'
    f'Дата окончания: {dict_note['issue_date']} \n'
    f'Заголовок: {dict_note['title']} \n')

# Ввод нового статуса заетки
print(f'Текущий статус заметки - {dict_note['status']}')

while True:
    new_status = input(
    f'Каков новый статус заметки? (введите 1, 2 или 3):  \n'
    '1 - В процессе \n'
    '2 - Отложено \n'
    '3 - Выполнено \n')
    if new_status == '1' or new_status == '2' or new_status == '3':
        # print(f'корректный ввод')  # , введите корректный статус - 1, 2 или 3')
        break
    # new_status1 = input(f'Новый статус заметки? (введите 1, 2 или 3):  \n'
        # '1 - В процессе \n'
        # '2 - Отложено \n'
        # '3 - Выполнено \n')
        # print(f'некорректный ввод, введите корректный статус - {dict_note['status']}')
status = int(new_status)

# Заметка в новом статусе
print('Заметка в новом статусе: \n'
    f'Имя пользователя - {dict_note['username']} \n'
    f'Описание заметки - {dict_note['content']} \n'
    f'Новый статус заметки - {dict_status[status]} \n' # 3 - Выполнено
    f'Дата создания: {dict_note['reated_date']} \n'
    f'Дата окончания: {dict_note['issue_date']} \n'
    f'Заголовок: {dict_note['title']} \n')

# Введение еще одного (или не одного) статуса при необходимости
while True:
    status1 = input('\nХотие ввести еще дополнительный статус заметки?: (Да/Нет?) ')
    if status1 == 'Нет' or status1 == 'нет' or status1 == 'н':
        print('\nНовых статусов у заметки нет')
        for key, value in dict_status.items():
            print(f'{key}: {value}')
        break
    status2 = input('Введите еще один статус заметки: ')
    len_dict_status = str(len_dict_status + 1)
    dict_status[len_dict_status] = status2
    len_dict_status = int(len_dict_status)
# # Новые статусы заметки
    print(f'\nНовые статусы заметки:')
    for key, value in dict_status.items():
        print(f'{key}: {value}')
