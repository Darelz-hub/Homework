# ЗАДАНИЕ
# Напишите программу на языке python, которая должна
# Создать бд shopIT
# Создать таблицу Компьютеры ( тип (ноутбук, стационарный компьютер, моноблок и т.д.), бренд, стоимость )

# Сделать ЗАПРОСЫ и отобразить в консоле:
# ●	показать все компьютеры бренда “HP” 
# (*усложненный вариант (НЕ ОБЯЗАТЕЛЬНО) HP может написано как HP, hp, Hp, Hp и в таких случаях все равно запрос должен отобразить все компьютеры бренда “HP”)
# ●	показать компьютеры стоимость которых более 40000
# ●	показать компьютеры типа “ноутбук” и стоимостью менее 30000

import sqlean as sqlite3
# sqlite3.extensions.enable('regexp')
#import sqlite3

with sqlite3.connect('shopIT.db') as con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS computer')
    cur.execute('''Create table computer(
        id integer not null primary key autoincrement,
        typeC text not null,
        brandC text not null,
        price int(10)
    );
                
                ''')
    cur.execute('''insert into computer(typeC,brandC,price) values
                ('Ноутбук',"hp",100000),
                ('ПК','Acer',20000),
                ("ноутбук","HP", 15000),
                ("Пк","Hp",60000)
                ''')
    result = cur.execute('''
                         select * from computer where brandC LIKE 'hp';
                         ''')
    for row in result.fetchall():
        print(row)
    
    result1 = cur.execute('''
                          select * from computer where price > 40000
                          ''')
    print('----------------------------------------------------------------')
    for row in result1.fetchall():
        print(row)
    
    print('----------------------------------------------------------------')
    result2 = cur.execute('''
                          select * from computer where typeC LIKE '%оутбук' and price < 30000;
                          ''')
    for row in result2.fetchall():
        print(row)
