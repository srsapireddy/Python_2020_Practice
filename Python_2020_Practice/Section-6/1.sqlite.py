import sqlite3 as sql

database = sql.connect('table1.db')

cursor = database.cursor()

# cmd = "CREATE TABLE users_rahul0457(username TEXT,password TEXT)"
cmd1 = 'INSERT INTO users_rahul0457 VALUES ("username_test","password_test")'
cmd2 = "SELECT username,password FROM users_rahul0457"

# cursor.execute(cmd)
cursor.execute(cmd1)
cursor.execute(cmd2)

database.commit()

for x in cursor:
    print x
