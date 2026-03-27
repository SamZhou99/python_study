import sqlite3
import random

connect = sqlite3.connect("database.sqlite")


def create_table():
    with connect:
        connect.execute(
            """CREATE TABLE IF NOT EXISTS user_list(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nick_name TEXT NOT NULL, 
            age INTEGER NOT NULL);"""
        )


def add_data():
    nick = "peter_" + str(random.randint(1, 999999))
    age = 18
    with connect:
        connect.execute(
            """INSERT INTO user_list (nick_name, age) VALUES (?, ?)""", (nick, age)
        )


def show_data():
    table_name = "user_list"
    cursor = connect.execute("""SELECT * FROM user_list ORDER BY id DESC LIMIT 10;""")
    count = connect.execute("""SELECT COUNT(*) AS total FROM user_list""")
    return count, cursor


def view_data(alldata):
    print(alldata[0])
    for item in alldata[1]:
        print(item)


def update_date(user_id):
    nick = "sam_" + str(random.randint(100000, 999999))
    age = 20
    with connect:
        connect.execute(
            """UPDATE user_list SET nick_name=?, age=? WHERE id=? """,
            (nick, age, user_id),
        )


def del_data(user_id):
    with connect:
        connect.execute("""DELETE FROM user_list WHERE id=? ;""", (user_id,))


def init():
    # create_table()
    # for i in range(100):
    #     add_data()
    # view_data(show_data())
    # update_date(1)
    # for i in range(40, 50):
    #     del_data(i)
    # print("==============")
    view_data(show_data())


init()
