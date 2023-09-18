
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
# # и вставить в них данные из файлов
# # https://github.com/makarova1507ana/python323/tree/main/SQL/%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%B5%20%D1%84%D0%B0%D0%B9%D0%BB%D1%8B 
import sqlite3
Salespeople = []
Customer = []
with open('salespeople.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        line = line.split(',')
        Salespeople.append(tuple(line))
with open('customers.txt', 'r',encoding="utf-8") as f:
    for line in f.readlines():
        line = line.split(',')
        Customer.append(tuple(line))
with sqlite3.connect('shops.db') as con:
    cur = con.cursor()
    cur.execute('Drop table if exists salespeople')
    cur.execute('Drop table if exists customers')
    cur.executescript('''
                Create table if not exists salespeople(
                    id integer primary key autoincrement,
                    sname text,
                    city text,
                    comm integer
                );
                Create table if not exists customers(
                    id integer primary key autoincrement,
                    cname text,
                    city text,
                    rating integer,
                    id_sp integer,
                    FOREIGN KEY(id_sp) references salespeople(id)
                );
                ''')
    #print(Salespeople)
    for el in Salespeople:
        cur.execute('insert into salespeople values (null,?,?,?)', (el[0], el[1], el[2]))
            #cur.execute('insert into salespeople nametable(****) values (sname,city,comm)', (line[0], line[1], line[2]))
    for el in Customer:
        cur.execute('insert into customers values (null,?,?,?,?)',(el[0], el[1], el[2], el[3]))
            
    
    # with open('customer.txt', 'r') as f:
    #     for line in f.readlines():
    #         line = line.split()
    #         cur.execute('insert into customers values (cname,city,rating,id_sp)', (line[0],line[1],line[2],line[3]))
    result = cur.execute("""
                SELECT * FROM salespeople,customers where customers.id_sp = salespeople.id and customers.city Like'%Москва'
                """) 
    for row in result.fetchall():
        print(row)
