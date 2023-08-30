from functional import AddContact, ShowAll, SearchContact, ChangeContact

def Choose(ent):
    if ent == '1': AddContact(input("Введите ваши данные пример:(фамилия имя отчество номер телефона) "))
    if ent == "2": ShowAll()
    if ent == "3": SearchContact(input("Введите имя, фамилию, отчество "))
    if ent == "4": ChangeContact(input("Какой контакт заменить? (имя фамилия) "), True)
    if ent == '5': ChangeContact(input('Какой контакт удалить? (имя фамилия) '), False)
    if ent == "6": print ("\n" + "Работа завершена!" + "\n"), exit()

def print_instructions():
    return print('Выберите действие: \n 1 - Добавить контакт \n 2 - Вывод всех контактов на экран \n '
                 '3 - Поиск по фамилии \n 4 - Редактировать данные контакта \n '
                 '5 - Удалить контакт \n 6 - Завершение работы')

