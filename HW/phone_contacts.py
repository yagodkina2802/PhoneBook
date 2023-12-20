import json

comands = ['add', 'show', 'edit', 'delete', 'close']
name = " "
phones = ' '
birthday = ' '
email = ' '
contact = {name: { "phones":[ ], 
                     ("birthday"): ' ', "email": ' '}}

def save():
    with open("contacts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(dict_tel, ensure_ascii=False))
    print("Изменения успешно сохранены!")

def edit(phonebook):
    redactor = input("Введите имя, которое хотите исправить : ")
    for name in list(phonebook):
        if redactor == name:
            temp_name = input("Введите новое имя:")
            phonebook[temp_name] = phonebook.pop(name)
            save()
            break
    else:
        print("Такого контакта не существует")
        

def delete(phonebook):
    redactor = input("Введите Контакт, который хотите удалить: ")
    for name in list(phonebook):
        if redactor == name:
            del phonebook[name]
            save()
            break
    else:
        print("Такого контакта не существует")

   
def load():
    try:
        with open("contacts.json", "r", encoding="utf-8") as fh:
            temp_contact = json.loads (fh.read())
            print(" ")
    except:
        print("Загрузка тестоваой телефонной книги")
        temp_contact = {'Igor': {"phones": [342, 4444], 
                        "birthday": "03.02.2003", "email": "12@ya.ru"},
                        "Petya": {"phones": [21548]}}
        with open("contacts.json", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(temp_contact, ensure_ascii=False))
        print("Загрузка прошла успешно")
    return temp_contact

dict_tel = load()

print("Вам доступны следующие команды:", *comands)

while True:
    comand = input("Введите команду: ")
    match(comand):
        case "add":
            while True:
                name = input("Введите имя: ") 
                phones = input("Введите номера телефонов через робел: ").split()
                answer = input("Желаете ввести дополнительную информацию о контакте? (Ответ Yes/No): ")
                if answer == 'Yes':
                    birthday = input("Введите дату рождения контакта: ")
                    email = input("Введите EMAIL: ")
                else:
                    birthday = ' '
                    email = ' '
                contact = {name: { "phones": phones, 
                     ("birthday"): birthday, "email": email}}
                dict_tel.update(contact)
                save()
                break

        case "show":
            for name, values in dict_tel.items():
                print(name, values)
        case "edit":
            edit(dict_tel)
        case "delete":
            delete(dict_tel)
        case 'close':
            break

