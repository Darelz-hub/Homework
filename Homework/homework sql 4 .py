# создать таблицы для бд как на изображении
# Можно воспользоваться запросом на вставку данных или придумать свои
# INSERT INTO players (name, best_score) VALUES (“Миша”,200),
# (“Ваня”,154),
# (“Дима”,178),
# (“Коля”,210);
# INSERT INTO games (name, score, id_player) VALUES 
# (“Миша”,110,1),
# (“Миша”,200,1),
# (“Дима”,178),
# (“Коля”,10),
# (“Коля”,30),

import sqlite3 as sq
with sq.connect('games.db') as con:
    cur = con.cursor()
    cur.execute('drop table players')
    cur.execute('drop table games')
    cur.executescript('''
                      Create table  if not exists players(
                        id integer not null primary key autoincrement,
                        name text not null,
                        best_score integer not null
                        );
                      Create table if not exists games(
                          id integer not null primary key autoincrement,
                          name text not null,
                          score integer not null,
                          id_players integer,
                          foreign key (id_players) references players(id)
                      );
                      ''')
    cur.execute('''insert into players(name,best_score) values
    ('Миша',200),
    ('Ваня',154),
    ('Дима',178),
    ('Коля',210);
    ''')
    cur.execute('''
                insert into games (name,score, id_players) values 
                ('Миша',110,1),
                ('Миша',200,1),
                ('Дима',178,3),
                ('Коля',10,4),
                ('Коля',30,4),
                ('Коля',40,4),
                ('Ваня',154,2),
                ('Коля',210,4);
                ''')
    # ●	показать игроков и их кол-во игр
    result = cur.execute('''
                         select name, count(id) from games  group by name
                         ''')
    for row in result.fetchall():
      print(row)
    print('----------------------------------------------------------------')
    #●	показать игроков и их итоговый счет за все сыгранные игры
    result1 = cur.execute('''
                         select name, sum(score) from games group by name
                         ''')
    for row in result1.fetchall():
      print(row)
    print('----------------------------------------------------------------')
    #●	Найти общее кол-во игр
    result3 = cur.execute('''
                          select count(id) from games
                          ''')
    print(result3.fetchone())
    print('----------------------------------------------------------------')
    
    #●	Найти худший результат у каждого игрока
    result4 = cur.execute('''
                          select name, min(score) from games group by name
                          ''')
    for row in result4.fetchall():
      print(row)