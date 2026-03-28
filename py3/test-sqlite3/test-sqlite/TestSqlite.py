import time
from ClassSqlite import ClassSqlite

SQLite = ClassSqlite("./test.sqlite")

# # SQLite.dropTable("file_list")

# SQLite.addField("name", SQLite.FIELD_TEXT)
# SQLite.addField("md5", SQLite.FIELD_TEXT)
# SQLite.addField("update_ts", SQLite.FIELD_INTEGER)
# SQLite.createTable("file_list")

# for i in range(10):
#     sql = "INSERT INTO file_list (`name`, `md5`, `update_ts`) VALUES ('TestFileName{}', 'TestMD5', {});".format(
#         i, round(time.time())
#     )
#     SQLite.execute(sql)

res = SQLite.select("SELECT COUNT(0) AS total FROM file_list")
print(res[0]["total"])

res = SQLite.select("SELECT * FROM file_list")
for i in res:
    print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(i["update_ts"])))

SQLite.finish()
