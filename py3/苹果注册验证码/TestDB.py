# from db.DB import DB
from db.MysqlDBTable import MysqlDBTable

data = [
    {
        "ip": "127.0.0.1:80",
        "status": 0,
        "create_datetime": MysqlDBTable.localtime,
        "update_datetime": MysqlDBTable.localtime,
    },
    {
        "ip": "127.0.0.1:80",
        "status": "0",
        "create_datetime": MysqlDBTable.localtime,
        "update_datetime": MysqlDBTable.localtime,
    },
    {
        "ip": "127.0.0.1:80",
        "status": "0",
        "create_datetime": MysqlDBTable.localtime,
        "update_datetime": MysqlDBTable.localtime,
    },
]


# db = DB()
# res = db.Select("SELECT * FROM proxy_ip_list LIMIT 10")
# for item in res:
#     print(item["title"])


# # 初始化
# proxyIpListTabel = DBTable("proxy_ip_list")

# # 增
# res = proxyIpListTabel.Add(data)

# # 改
# proxyIpListTabel.Update(12, {"status": 1, "ip": "0.0.0.0:8080"})

# # 删
# proxyIpListTabel.Delete(13)

# # 查
# setValue = proxyIpListTabel.Select("ORDER BY id DESC LIMIT 10")
# for item in setValue:
#     print(item["id"])
