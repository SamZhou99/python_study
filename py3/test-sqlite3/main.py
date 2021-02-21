import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect("test.db")
conn.row_factory = dict_factory
print("sqlite open")

user_list = conn.cursor().execute("""SELECT * FROM user_info LEFT JOIN user_categorys ON user_info.category_id=user_categorys.id""")
for user_item in user_list:
    print(user_item)
    sql = """SELECT * FROM user_info LEFT JOIN sales_order ON sales_order.user_id=user_info.id WHERE user_info.id={}""".format(user_item['id'])
    user_sales_order = conn.cursor().execute(sql)
    for order_item in user_sales_order:
        print(order_item)

conn.commit()
conn.close()
