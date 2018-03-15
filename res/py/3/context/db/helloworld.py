import dataset
class ${Name}:
    def __init__(self):
        pass

    def Run(self):
        path = ':memory:' # /tmp/example.db
        db = dataset.connect('sqlite:///' + path)
        db.begin()
        self.__Query(db)
        self.__Method(db)
        db.commit()

    def __Query(self, db):
        db.query('''create table Human (
            Id      integer primary key,
            Name    text,
            Age     integer
        );''')
        db.query("insert into Human (Name, Age) values ('Bob', 20);")
        for row in db.query("select * from Human;"): print(row)
        db.query("update Human set Age=33 where Name='Bob';")
        for row in db.query("select * from Human;"): print(row)
        db.query("delete from Human where Name='Bob';")
        for row in db.query("select * from Human;"): print(row)

    def __Method(self, db):
        import sqlalchemy.types
        table_name = 'Human'
        db[table_name].drop()
        # "id"を"Id"にしたいのにできない！ 勝手にautoincrementになる！
        db.create_table(table_name, primary_id='Id', primary_type=db.types.integer) # sqlalchemy.types.Integer ?
        print(db[table_name].columns)
        column_defines = {'Name': sqlalchemy.types.Text, 'Name': sqlalchemy.types.Text, 'Age': sqlalchemy.types.Integer}
        for name, type in column_defines.items():
            db[table_name].create_column(name, type)
        print(db[table_name].columns)

        db[table_name].insert(dict(Name='Bob', Age=20))
        print(db[table_name].find_one(Name='Bob'))
        print(db[table_name].find(Name='Bob').next())
        db[table_name].update(dict(Age=33, Name='Bob'), ['Name'])
        print(db[table_name].find_one(Name='Bob'))
        db[table_name].delete(Name='Bob')
        print(db[table_name].find_one(Name='Bob'))


if __name__ == '__main__':
    c = ${Name}()
    c.Run()
    c.Run()

    
