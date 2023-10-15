'''
Результат 
ССЫЛКА на гитхаб  
 
последняя практика 
https://github.com/makarova1507ana/python323/tree/main/work_with_git
 
Начиная с этого дз вам разрешается вести работу в команде (2+ людей)
Если вы ведете такую работу, обязательно в репозиторий выложить файл readme.md с указанием вашей работы

Пример уже реализованного проекта (вам конечно все в консоле нужно делать)
https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 

ЗАДАНИЕ
Необходимо создать программу по созданию учетных записей для банка, открытие счета для пользователя 

Какой необходимо реализовать функционал
●	Добавление пользователя (имя, фамилия, почтовый код, открытые счета)
●	Открытие счета для пользователя, счет можно открыть в разных валютах:
○	Dollar 
○	Pound
○	Rupee
●	Просмотр учетных записей
Можете оформлять коммиты и ветки в свободном стиле, главное загрузить все на github и поделиться в дз ссылкой на репозиторий 
'''
import sqlite3 as sq
from users import Users
with sq.connect('bank.db') as con:
    cur = con.cursor()
    cur.execute('''
                create table if not exists users
                (
                    id integer primary key autoincrement,
                    name text,
                    cname text,
                    postal_code text,
                    bankAccount text default null
                );
                ''')

    while True:
        print('''
              Что вы хотите сделать?
              1. Добавить нового пользователя
              2. Открыть счёт пользователю
              3. Просмотреть записи
              4. Завершить работу
              ''')
        people_choise = int(input('Введите ваше действие: '))
        
        if people_choise == 1:
            user = Users(input('Введите имя'),input('Введите фамилию '),input('Введите почтовый код'))
            cur.execute(f'insert into users(name,cname,postal_code) values ("{user.name}","{user.cname}","{user.postal_code}");')
        
        elif people_choise == 2:
            print('''Выберите нужного пользователя
----------------------------------------------------------------------------------------------------------------------------''')
            result = cur.execute('select * from users')
            for row in result.fetchall():
                print(row)
            
            id = int(input('Ваш выбор, введите его id: '))
            people_choise = int(input('''В чём хотите открыть вклад?
                                  1. Dollar
                                  2. Pound
                                  3. Rupee
                                  '''))
           
            if people_choise == 1:
                cur.execute(f'update users set bankAccount = "Dollar"  where id = "{id}" ')
          
            elif people_choise == 2:
                cur.execute(f'update users set bankAccount = "Pound"  where id = "{id}" ')  
            
            elif people_choise == 3:
                cur.execute(f'update users set bankAccount = "Rupee"  where id = "{id}" ')
                    
        elif people_choise == 3: 
            result = cur.execute('select * from users')
            for row in result.fetchall():
                print(row)
        
        elif people_choise == 4:
            print('Работа завершена')
            break