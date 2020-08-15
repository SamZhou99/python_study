from __future__ import division
import datetime
import pymysql
import time
import urllib.request
import requests
import chardet

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'lajiao_video',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
mysql_conn = pymysql.connect(**config)


def close():
    mysql_conn.close()


def insert(title, age, timedate):
    sql = "INSERT INTO `test`.`content`(`title`, `age`, `timedate`) VALUES ('{0}', '{1}', '{2}')".format(
        title, age, timedate)
    print(sql)
    cursor = mysql_conn.cursor()
    cursor.execute(sql)
    cursor.close()


def execute(db, sql, data=None):
    try:
        cursor = db.cursor()
        cursor.execute(sql, data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return True


def executemany(db, sql, data):
    try:
        cursor = db.cursor()
        cursor.executemany(sql, data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return True


def updateUrlToM3u8(item):
    url = item['video']
    domain = url[:url.find('/', 8)]

    # response = urllib.request.urlopen(url)
    # html = response.read()
    # charset = chardet.detect(html)['encoding']
    # html = html.decode(charset)
    # print(charset)

    try:
        response = requests.get(url)
    except:
        print('请求异常', url)
        return False

    html = response.text
    start_str = '{"url":"'
    end_str = '"}]'
    start_num = html.find(start_str)
    end_num = html.find(end_str, start_num)
    m3u8_url = html[start_num+len(start_str):end_num]
    m3u8_url = domain+m3u8_url
    print(item['id'], m3u8_url)

    sql = "UPDATE articles SET video='{1}' WHERE id={0}".format(
        item['id'], m3u8_url)
    execute(mysql_conn, sql)


max_id = 96822


def select():
    global max_id
    sql = "SELECT * FROM articles WHERE id<{1} AND source_site='wles2.xyz' ORDER BY id DESC LIMIT {0}".format(
        '30', max_id)
    print(sql)
    with mysql_conn.cursor() as cursor:
        cursor.execute(sql)
        result_list = cursor.fetchall()
        for item in result_list:
            print('\r\n')
            item['video'] = item['video'].replace(
                'https://2.dadi-yun.com/', 'https://2.ddyunbo.com/')
            item['video'] = item['video'].replace(
                'https://dadi-yun.com/', 'https://2.ddyunbo.com/')
            print(item['id'], item['video'])
            if item['video'].rfind('.m3u8') == -1:
                updateUrlToM3u8(item)

        time.sleep(1)
        max_id = result_list[len(result_list)-1]['id']
        print('\r\n')
        select()


# insert('标题', 9, time.strftime('%Y-%m-%d %M:%I:%S', time.localtime()))
select()
close()
