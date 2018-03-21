import sqlite3
conn = sqlite3.connect(':memory:') # /tmp/example.db
c = conn.cursor()
c.execute('''create table Human (
    Id      integer primary key,
    Name    text,
    Age     integer
);''')
c.execute("insert into Human (Name, Age) values ('Bob', 20);")
for row in c.execute("select * from Human;"): print(row)
c.execute("update Human set Age=33 where Name='Bob';")
for row in c.execute("select * from Human;"): print(row)
c.execute("delete from Human where Name='Bob';")
for row in c.execute("select * from Human;"): print(row)
conn.commit()
conn.close()
