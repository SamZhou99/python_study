from config.db import DB_Config
import pymysql


class MysqlDB:
    def __init__(self) -> None:
        config = DB_Config()
        self.mysql_conn = pymysql.connect(**config.mysql)

    def Close(self):
        self.mysql_conn.close()

    def Query(self, sql):
        cursor = self.mysql_conn.cursor()
        cursor.execute(sql)
        cursor.close()

    def Select(self, sql):
        with self.mysql_conn.cursor() as cursor:
            cursor.execute(sql)
            result_list = cursor.fetchall()
            cursor.close()
            return result_list


# class DBTable:
#     def __init__(self, table) -> None:
#         self.table = table
#         self.db = DB()

#     def Close(self):
#         return self.db.Close()

#     def Add(self, fieldArrDic):
#         if len(fieldArrDic) > 2:
#             for item in fieldArrDic:
#                 sql = "INSERT INTO `{}`(`{}`) VALUES ('{}')".format(
#                     self.table, fieldArrDic
#                 )
#         else:
#             sql = "INSERT INTO `{}`({}) VALUES ({})".format(self.table, fieldArrDic)
#         return self.db.Query(sql)

#     def Delete(self, id):
#         sql = "DELETE FROM `{}` WHERE id={}".format(self.table, id)
#         return self.db.Query(sql)

#     def Update(self, id):
#         sql = "UPDATE INTO `{}` WHERE id={}".format(self.table, id)
#         return self.db.Query(sql)

#     def Select(self, where):
#         sql = "SELECT * FROM {} WHERE {}".format(self.table, where)
#         return self.db.Select(sql)
