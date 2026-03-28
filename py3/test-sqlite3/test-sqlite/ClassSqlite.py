import os
import sqlite3


class ClassSqlite:
    # 静态变量
    FIELD_TEXT = "TEXT"
    FIELD_INTEGER = "INTEGER"

    # 构造
    def __init__(self, sqlite_file_path) -> None:
        if os.path.isfile(sqlite_file_path):
            self.__init(sqlite_file_path)
        else:
            print("ClassSqlite: {} 找不到文件。".format(sqlite_file_path))

    # 初始化
    def __init(self, sqlite_file_path) -> bool:
        self.fields = []
        self.conn = sqlite3.connect(sqlite_file_path)
        self.conn.row_factory = self.__dict_factory
        self.cursor = self.conn.cursor()
        return True

    # 添加字段
    def addField(self, name: str, type: str) -> bool:
        self.fields.append("{} {}".format(name, type))
        return True

    # 创建表
    def createTable(self, tabel_name: str) -> bool:
        if self.__check_tabel_exist(tabel_name):
            # print("【{}】表已存在。".format(tabel_name))
            return False

        if self.__check_field_exist(tabel_name, self.fields):
            return False

        fields = ", ".join(self.fields)
        self.cursor.execute("CREATE TABLE {}({})".format(tabel_name, fields))
        return True

    # 执行SQL
    def execute(self, sql: str) -> sqlite3.Cursor:
        return self.cursor.execute(sql)

    # 查询
    def select(self, sql: str):
        self.execute(sql)
        result = self.cursor.fetchall()
        # for row in result:
        #     print(row)
        return result

    # 删除丢弃表
    def dropTable(self, tabel_name) -> bool:
        sql = "DROP TABLE {};".format(tabel_name)
        self.execute(sql)
        return True

    # 提交&关闭链接
    def finish(self) -> bool:
        self.conn.commit()
        self.conn.close()
        return True

    # 检查表是否存在
    def __check_tabel_exist(self, tabel_name: str) -> bool:
        sql = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        tables = self.execute(sql)
        for i in tables:
            if i["name"] == tabel_name:
                return True
        return False

    # 检查字段是否存在
    def __check_field_exist(self, tabel_name: str, fields: list) -> bool:
        sql = "PRAGMA table_info([{}]);".format(tabel_name)
        fields_res = self.execute(sql)
        for field_row in fields_res:
            for field_item in fields:
                print("xxxxxxxxxxxxxxxxx", field_row)
                if field_row[1] == field_item.split()[0]:
                    # print("【{}.{}】字段表已存在。".format(tabel_name, field_row[1]))
                    return True
        return False

    # @staticmethod
    def __dict_factory(self, cursor, row):
        # 将游标获取的数据处理成字典返回
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
