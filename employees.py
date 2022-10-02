import actions as act
 
 
def choice():
    while True:
        text = input('Выберите действие с данными: 1 - добавить, 2 - удалить, 3 - просмотреть все записи, 4 - найти, 5 - редактировать, 6 - показать среднюю зарплату списка, 7 - выйти: ')
        if text == '1':
            act.write_data()
            print('Запись добавлена.')
        elif text == '2':
            identifier = input('Введите id для удаления данных: ')
            act.delete_data(identifier)
        elif text == '3':
            act.view_data()
        elif text == '4':
            search_type = input('Введите поле, по которому производим поиск: 1 - ID сотрудника, 2 - фамилия')
            if search_type == '1':
                find_id = input('Введите ID: ')
                act.find_data_id(find_id)
            else: 
                find_surname = input('Введите фамилию: ')
                act.find_data_surname(find_surname)
        elif text == '5':
            identifier = input('Введите id для редактирования данных: ')
            current = int(input('Что меняем: 1 - Фамилия, 2 - Имя, 3 - Телефон, 4 - Должность: '))
            new = input('Введите новую запись: ')
            act.edit_data(identifier, current, new)
            print('Запись отредактирована.')
        elif text == '6':
            print(f'Средняя зарплата сотрудников: {act.avg_salary()}')
        elif text == '7':
            break
        else:
            print('Введена некорректная команда.')

# choice()