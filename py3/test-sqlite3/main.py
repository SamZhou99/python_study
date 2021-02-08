import sqlite3

conn = sqlite3.connect("test.db")
print("sqlite open")

user_res = c = conn.cursor().execute("""SELECT * FROM user_info LEFT JOIN user_categorys ON user_info.category_id=user_categorys.id""")
for user_row in user_res:
    print(user_row)
    sales_order = conn.cursor().execute("""SELECT * FROM sales_order LEFT JOIN user_info ON user_info.id=sales_order.user_id WHERE sales_order.user_id=1 """)
    for order_row in sales_order:
        print(order_row)

conn.commit()
conn.close() 