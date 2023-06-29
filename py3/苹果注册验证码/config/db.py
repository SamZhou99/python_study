import pymysql


class DB_Config:
    def __init__(self):
        self.mysql = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "root",
            "db": "apple_id",
            "charset": "utf8mb4",
            "cursorclass": pymysql.cursors.DictCursor,
        }
        self.sqlite_sms = "./sms.db"
        self.sqlite_english_name = "./english_name/names.db"

    def __str__(self) -> str:
        return self.mysql
