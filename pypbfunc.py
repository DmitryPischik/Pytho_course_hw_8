# создаем функцию для добавления новой записи
def add_data(data):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data.append({'last_name': last_name, 'first_name': first_name, 'patronymic': patronymic, 'phone_number': phone_number})
    print('Запись добавлена успешно')
# создаем функцию для экспорта данных в файл
def export_data(filename, data):
    try:
        with open(filename, 'w') as f:
            for d in data:
                f.write(','.join([d['last_name'], d['first_name'], d['patronymic'], d['phone_number']]) + '\n')
            print('Данные экспортированы успешно')
    except:
        print('Ошибка при экспорте данных')
# создаем функцию для импорта данных из файла
def import_data(filename):
    try:
        with open(filename, 'r') as f:
            data = f.readlines()
            data = [d.strip() for d in data]
            contacts = []
            for d in data:
                contact = d.split(',')
                contacts.append({'last_name': contact[0], 'first_name': contact[1], 'patronymic': contact[2], 'phone_number': contact[3]})
            print('Данные импортированы успешно')
            return contacts
    except FileNotFoundError:
        print('Файл не найден')
# создаем функцию для поиска записей по заданной характеристике
def search_data(data):
    select = input('Введите характеристику для поиска (1 - Фамилия, 2 - Имя, 3 - Отчество или 4 - Номер телефона): ')
    if select in ['1', '2', '3', '4']:
        if select == '1':
            attribute = 'last_name'
        elif select == '2':
            attribute = 'first_name'
        elif select == '3':
            attribute = 'patronymic'
        else:
            attribute = 'phone_number'
        value = input('Введите значение: ')
        results = [d for d in data if d[attribute] == value]
        return results
    else:
        print('Неверный ввод')    
# создаем функцию для удаления записи
def delete_data(data):
    matches = search_data(data)
    if not matches:
        print('Запись не найдена')
        return data
    elif len(matches) > 1:
        print('Найдено несколько записей:')
        for i, match in enumerate(matches):
            print(f"{i + 1}. {match['last_name']} {match['first_name']} {match['patronymic']}: {match['phone_number']}")
        choice = int(input('Введите номер записи для удаления: '))
        selected = matches[choice - 1]
    else:
        selected = matches[0]
    print(f"Выбрана запись для удаления: {selected['last_name']} {selected['first_name']} {selected['patronymic']}: {selected['phone_number']}")
    yes_no = input('Вы действительно хотите удалить эту запись? да/нет: ')
    if yes_no == 'да':
        data = [line for line in data if line != selected]
        print('Запись удалена')
    elif yes_no == 'да':
        print('Запись не удалена')
    else:
        print('Неверный ввод')
    return data
# функция для изменения записи
def edit_data(data):
    matches = search_data(data)
    if not matches:
        print('Запись не найдена')
        return data
    elif len(matches) > 1:
        print('Найдено несколько записей:')
        for i, match in enumerate(matches):
            print(f"{i + 1}. {match['last_name']} {match['first_name']} {match['patronymic']}: {match['phone_number']}")
        choice = int(input('Введите номер записи для редактирования: '))
        selected = matches[choice - 1]
    else:
        selected = matches[0]
    print(f"Выбрана запись для удаления: {selected['last_name']} {selected['first_name']} {selected['patronymic']}: {selected['phone_number']}")
    new_data = []
    for line in data:
        if line == selected:
            new_data.append({'last_name': input('Введите новую фамилию: '), 'first_name': input('Введите новое имя: '), 'patronymic': input('Введите новое отчество: '), 'phone_number': input('Введите новый номер телефона: ')})
        else:
            new_data.append(line)
    print('Запись изменена успешно')
    return new_data
