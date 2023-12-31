#Телефонный справочник
#work_with_phonebook():

def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Закончить работу\n' )
          #'7. Закончить работу\n', sep = '\n' )
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while(choice!=7):

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname')
            new_number = input('new_number')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('lastname')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('number')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        choice = show_menu()


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия','Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding = 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open('phonebook.txt', 'w', encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f',{s[:-1]}\n')

#1. Распечатать справочник
def print_result(phone_book):
     for x in range(len(phone_book)):
        for key, value in phone_book[x].items():
            print(key,':', value)

#2. Найти телефон по фамилии
def find_by_lastname(phone_book, last_name):
     for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия').lower() == last_name.lower():
            return 'Телефон:' + phone_book[i].get('Телефон').lower()
        else:
            return 'Такой фамилии нет в справочнике'

#3. Изменить номер телефона
def change_number(phone_book, last_name, new_number):
     for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия').lower() == last_name.lower():
            phone_book[i].update({'Телефон': new_number})
        write_txt('phonebook.txt',phone_book)
    

#5. Найти абонента по номеру телефона
def find_by_number(phone_book, number):
     for i in range(len(phone_book)):
        if phone_book[i].get('Телефон') == number:
            return phone_book[i].get('Фамилия')
        
#4. Удалить запись
def delete_by_lastname(phone_book, last_name):
     for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия') == last_name:
            del phone_book[i] 
            break
        write_txt('phonebook.txt',phone_book)
        
work_with_phonebook()



