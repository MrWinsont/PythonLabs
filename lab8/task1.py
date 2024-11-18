import sqlite3 as sl

conn = sl.connect('orders.db')
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS courier(
                courier_id     INT PRIMARY KEY,
                surname        TEXT,
                name           TEXT,
                middle_name    TEXT,
                passport_id    TEXT,
                birth_date     TEXT,
                hiring_date    TEXT,
                start_work_day TEXT,
                end_work_day   TEXT,
                city           TEXT,
                street         TEXT,
                house          TEXT,
                flat           TEXT,
                phone          TEXT);
            """)

cur.execute(""" CREATE TABLE IF NOT EXISTS sender(
                sender_id      INT PRIMARY KEY,
                surname        TEXT,
                name           TEXT,
                middle_name    TEXT, 
                birth_date     TEXT,
                Ind            TEXT,
                city           TEXT,
                street         TEXT,
                house          TEXT,
                flat           TEXT,
                phone          TEXT);
            """)

conn.commit()

cur.execute("""INSERT INTO 
            sender(sender_id, surname, name, middle_name, birth_date, Ind, city, street, house, flat, phone)
            VALUES(1, 'Ivanov', 'Stepan', 'Ioanovich', '15.04.2000', '2',
             'Pskov', 'Shorsa', '3', '1', '+7911124536');
            """)
conn.commit()

courier = (1, 'Petrov', 'Ivan', 'Fedorovich', '49', '18.04.2000', '18.04.2024', '10:00', '18:00',
           'Ekatirinburg', 'Nevskogo', '2', '3', '+7911417283')

cur.execute("INSERT INTO courier VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", courier)
conn.commit()

cur.execute("""UPDATE sender
               set city = 'Kaliningrad'
               where sender_id = 1
           """)
conn.commit()


cur.execute("SELECT * FROM sender;")
one_result = cur.fetchone()
print(one_result)

conn.close()