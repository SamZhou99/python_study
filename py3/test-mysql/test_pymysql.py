import pymysql

mysql_conn = pymysql.connect(
    host= '127.0.0.1', 
    port= 3306, 
    user= 'root', 
    password= 'root', 
    db= 'jimo100'
)

def close():
    mysql_conn.close()

def select():
    sql = "SELECT * FROM articles WHERE a_ok='{0}' LIMIT 10".format('0')
    print(sql)
    with mysql_conn.cursor() as cursor :
        cursor.execute(sql)
        result_list = cursor.fetchall()
        for result_one in result_list:
            print(result_one)