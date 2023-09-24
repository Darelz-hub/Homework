
# # ЗАДАНИЕ
# # Создать таблицы  по их описанию
# # /*— для Salespeople
# # id(уникальный номер продавца)
# # sname (имя)
# # city (город)
# # comm (комиссионные)

# # — для Customers
# # id(уникальный номер заказчика)
# # cname (имя)
# # city (город)
# # rating (рейтинг)
# # id_sp(номер продавца, который обслуживает этого заказчика)*/
# Реализовать интерфейс для регистрации, редактирование и удаления записей о продавцах и заказчиков 
import sqlite3
import random 
Salespeople = []
Customer = []
# with open('salespeople.txt', 'r', encoding="utf-8") as f:
#     for line in f.readlines():
#         line = line.split(',')
#         Salespeople.append(tuple(line))
# with open('customers.txt', 'r',encoding="utf-8") as f:
#     for line in f.readlines():
#         line = line.split(',')
#         Customer.append(tuple(line))


def upper_salespeople(id_sp):
    print('Введите изменения продавца: ')
    result = cur.execute(f"""
            SELECT * FROM salespeople
            """)
    for row in result.fetchall():
        print(row)
    list_name = [input('Введите ФИО продавца'),input('Введите город продавца'),int(input('Введите коммиссионные: '))]
    cur.execute(f'''
                Update salespeople set sname = \'{list_name[0]}\',city = \'{list_name[1]}\', comm = \'{list_name[2]}\' where id = '{id_sp}'
                ''')
    
def upper_customers(id_c):
    print('Введите изменения продавца: ')
    result = cur.execute(f"""
            SELECT * FROM customers
            """)
    for row in result.fetchall():
        print(row)
    list_name = [input('Введите ФИО продавца'),input('Введите город продавца'),int(input('Введите рейтинг: '), int(input('Введите id продавца')))]
    cur.execute(f'''
                Update salespeople set sname = \'{list_name[0]}\',city = \'{list_name[1]}\', comm = \'{list_name[2]}\' where id = '{id_c}'
                ''')
def delete_salespeople(id_sp):
    cur.execute(f"""
                DELETE FROM salespeople WHERE id = '{id_sp}'
                """)
def delete_customers(id_c):
        cur.execute(f"""
                DELETE FROM customers WHERE id = '{id_c}'
                """)
def registration_user_salespeople(name):
    list_name = []
    name_user = name
    result = cur.execute(f"""
                SELECT name_user FROM salespeople WHERE name_user = \'{name_user}\'
                """) 
    #print(result.fetchall())
    
    while len(result.fetchall()) != 0:
        # проверка наличия пользователя
        print('Такой продавец уже существует, введите новое имя')
        name_user = input('Введите новое имя продавца: ')
        result = cur.execute(f"""
            SELECT name_user FROM salespeople WHERE name_user = \'{name_user}\'
                """)
      
    #passorwd = input('Введите пароль пользователя:')
    list_name = [name_user, input('Введите пароль продавца:'), input('Введите ФИО продавца: '), input('Введите город продавца: '),int(input('Введите коммиссионные: '))]
    cur.execute('insert into salespeople(name_user, password,sname,city, comm ) values (?,?,?,?,?)',(list_name[0], list_name[1], list_name[2], list_name[3], list_name[4]))
    result = cur.execute(f"""
            SELECT * FROM salespeople
            """)
    for row in result.fetchall():
        print(row)
def registration_user_customers(name):
    list_name = []
    name_user = name
    result = cur.execute(f"""
                SELECT name_user_c FROM customers WHERE name_user_c = \'{name_user}\'
                """) 
    #print(result.fetchall())
    
    while len(result.fetchall()) != 0:
        # проверка наличия пользователя
        print('Такой пользователь уже существует, введите новое имя')
        name_user = input('Введите новое имя пользователя: ')
        result = cur.execute(f"""
            SELECT name_user_c FROM customers WHERE name_user_c = \'{name_user}\'
                """)
      
    #passorwd = input('Введите пароль пользователя:')
    list_name = [name_user, input('Введите пароль пользователя:'), input('Введите ФИО продавца: '), input('Введите город пользователя: '),int(input('Введите рейтинг: ')), int(input('Введите id продавца'))]
    cur.execute('insert into customers(name_user_c, password_c,cname,city,rating, id_sp) values (?,?,?,?,?,?)',(list_name[0], list_name[1], list_name[2], list_name[3], list_name[4],list_name[5]))
    result = cur.execute(f"""
            SELECT * FROM customers
            """)
    for row in result.fetchall():
        print(row)

with sqlite3.connect('shops.db') as con:
    cur = con.cursor()
    # cur.execute('Drop table if exists salespeople')
    # cur.execute('Drop table if exists customers')
    cur.executescript('''
                Create table if not exists salespeople(
                    id integer primary key autoincrement,
                    name_user text,
                    password text,
                    sname text,
                    city text,
                    comm integer
                );
                Create table if not exists customers(
                    id integer primary key autoincrement,
                    name_user_c text,
                    password_c text,
                    cname text,
                    city text,
                    rating integer,
                    id_sp integer,
                    FOREIGN KEY(id_sp) references salespeople(id)
                );
                ''')

    while True:
            print('''Выберите таблицу для взаимодействия:
                1: salespeople
                2: customers''')
            choice = int(input('Введите ваш выбор: '))
            if choice == 1:
                print('''Вы в таблице salespeople.
                    Что вы хотите сделать?
                    1: зарегистрировать нового продавца
                    2: изменить данные
                    3: удалить данные''')
                user_choise = int(input('Введите ваш выбор: '))
                if user_choise == 1:
                    name = input('Введите имя продавца: ')
                    registration_user_salespeople(name)
                    break
                elif user_choise == 2:
                    upper_salespeople(int(input('Введите id продавца: ')))
                    break
                elif user_choise == 3:
                    delete_salespeople(int(input('Введите id продавца: ')))
                    break
                
                else:
                     break 
            elif choice == 2:
                print('''Вы в таблице customers.
                    Что вы хотите сделать?
                    1: зарегистрировать нового пользователя
                    2: изменить данные
                    3: удалить данные''')
                user_choise = int(input('Введите ваш выбор: '))
                if user_choise == 1:
                    name = input('Введите имя пользователя: ')
                    registration_user_customers(name)   
                    break
                elif user_choise == 2:
                    upper_customers(int(input('Введите id пользователя: ')))
                    break
                elif user_choise == 3:
                    delete_customers(int(input('Введите id покупателя: ')))
                    break
    # result = cur.execute(f"""
    #         SELECT * FROM salespeople
    #         """)
    # for row in result.fetchall():
    #                 print(row)
