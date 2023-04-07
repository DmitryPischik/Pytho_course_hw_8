"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
функционал для изменения и удаления данных
"""
from pypbfunc import *

def main():
    filename = 'contacts.txt'
    data = import_data(filename)
    while True:
        print('1. Вывести справочник на экран')
        print('2. Добавить запись')
        print('3. Удалить запись')
        print('4. Изменить запись')  
        print('5. Поиск записей')
        print('6. Выйти')
        choice = input('Выберите действие: ')
        if choice == '1':
            if len(data) == 0:
                print('Справочник пуст')
            else:
                for d in data:
                    print(f"{d['last_name']} {d['first_name']} {d['patronymic']}: {d['phone_number']}")
        elif choice == '2':
            add_data(data)
        elif choice == '3':
            data = delete_data(data)
        elif choice == '4':
            data = edit_data(data)        
        elif choice == '5':     
            results = search_data(data)
            if results:
                for r in results:                    
                    print(f"{r['last_name']} {r['first_name']} {r['patronymic']}: {r['phone_number']}")
            else:
                print('Записи не найдены')
        elif choice == '6':
            export_data(filename, data)
            break
        else:
            print('Неверный ввод')
if __name__ == '__main__':
    main()