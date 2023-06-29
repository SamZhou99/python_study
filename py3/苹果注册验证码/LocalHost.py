import json
import sqlite3
import time
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import abort
from flask_cors import CORS
from config.db import DB_Config

from phone_sms.PhoneNumberFormat import PhoneNumberFormat


class LocalHost:
    def __init__(self, port=6789) -> None:
        self.port = port
        self.app = Flask(__name__)
        CORS(self.app)

    def Route(self):
        @self.app.route("/")
        def index():
            return {"message": "api"}

        @self.app.route("/sms", methods=["POST"])
        def sms_post():
            d = dict(request.form)
            d.update({"ts": getTime()})
            # 提交过来的数据
            # msg : "Waiting for SMS"
            # phone_number : "+63 (985) 565 42 90"
            # price : "10.00 ₽"
            # time : "17 min"
            # ts : "2023-6-1 12:17:47"
            if d["msg"].find("waiting") > -1:
                return {"flag": "waiting"}
            PhoneFormat = PhoneNumberFormat()
            country_number, phone_number = PhoneFormat.formatPhone(d["phone_number"])
            sms_db = LocalSqliteSMS()
            rsp = sms_db.FindByPhoneCode(phone_number, d["msg"])
            if len(rsp) > 0:
                return {
                    "flag": "ok",
                    "msg": "数据有重复：{}, {}".format(d["phone_number"], d["msg"]),
                }
            phone_number = country_number + " " + phone_number
            status = 1
            code = d["msg"]
            tag = "sms-activate"
            ts = getTime()

            sms_db.Insert(status, phone_number, code, tag, ts)
            print(status, phone_number, code, tag, ts)
            return {"flag": "ok"}

        @self.app.route("/sms", methods=["GET"])
        def sms_get():
            sms_db = LocalSqliteSMS()
            l = sms_db.ListByDesc(5)
            li = []
            for i in l:
                li.append(i)
            return {"data": li}

        @self.app.route("/sms/<phone_number>/<date_time>", methods=["GET"])
        def sms_phone_get(phone_number, date_time):
            sms_db = LocalSqliteSMS()
            rsp = sms_db.FindByPhoneDatetime(phone_number, date_time)
            a = []
            for i in rsp:
                a.append(i)
            return {"data": a, "ts": getTime()}

        @self.app.route("/sms-last/<phone_number>", methods=["GET"])
        def sms_last_phone_get(phone_number):
            sms_db = LocalSqliteSMS()
            rsp = sms_db.FindByLastPhone(phone_number)
            a = []
            for i in rsp:
                a.append(i)
            return {"data": a, "ts": getTime()}

    def Run(self):
        self.app.run(host="0.0.0.0", port=self.port, debug=True)


class LocalSqliteSMS:
    def __init__(self) -> None:
        config = DB_Config()
        self.conn = sqlite3.connect(config.sqlite_sms)
        self.conn.row_factory = dict_factory

    def Test(self):
        list = self.Query("""SELECT * FROM sms_list LIMIT 1""")
        for item in list:
            print(item)

    def Query(self, sql):
        result = self.conn.cursor().execute(sql)
        self.conn.commit()
        return result

    def Insert(self, status, phone, code, tag, datetime):
        sql = """INSERT INTO sms_list(`status`, `phone`, `code`, `tag`, `datetime`) VALUES({},"{}","{}","{}","{}")""".format(
            status, phone, code, tag, datetime
        )
        return self.Query(sql)

    def Delete(self, id):
        sql = """DELETE FROM sms_list WHERE id={}""".format(id)
        return self.Query(sql)

    def UpdateStatus(self, id, status):
        sql = """UPDATE sms_list SET `status`={} WHERE id={}""".format(status, id)
        return self.Query(sql)

    def UpdateAllStatus(self, status=1):
        sql = """UPDATE sms_list SET `status`={}""".format(status)
        return self.Query(sql)

    def ListByDesc(self, limit=1) -> list:
        sql = """SELECT * FROM sms_list ORDER BY id DESC LIMIT {}""".format(limit)
        return self.Query(sql)

    def Count(self):
        sql = """SELECT COUNT(*) AS total FROM sms_list WHERE status=1"""
        return self.Query(sql)

    def Find(self, id) -> list:
        sql = """SELECT * FROM sms_list WHERE id={} LIMIT 1""".format(id)
        return self.Query(sql)

    def FindByPhoneCode(self, phone, code) -> list:
        sql = """SELECT * FROM sms_list WHERE phone LIKE "%{}%" AND code={} ORDER BY id DESC LIMIT 5""".format(
            phone, code
        )
        return list(self.Query(sql))

    def FindByPhoneLike(self, phone) -> list:
        sql = """SELECT * FROM sms_list WHERE phone LIKE "%{}%" ORDER BY id DESC LIMIT 5""".format(
            phone
        )
        a = []
        rsp = self.Query(sql)
        for i in rsp:
            a.append(i)
        return a

    def FindByLastPhone(self, phone) -> list:
        sql = """SELECT * FROM sms_list WHERE phone LIKE "%{}%" ORDER BY id DESC LIMIT 1""".format(
            phone
        )
        return self.Query(sql)

    def FindByPhoneDatetime(self, phone, date_time) -> list:
        sql = """SELECT * FROM sms_list WHERE phone LIKE "%{}%" AND datetime >= '{}' ORDER BY id DESC """.format(
            phone, date_time
        )
        return self.Query(sql)

    def Close(self):
        self.conn.close()


# 格式化日期时间
def getTime():
    t = time.localtime()
    return "{}-{}-{} {}:{}:{}".format(
        t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec
    )


# 数据库 数据 以 字典方式显示
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# sms_db = LocalSqliteSMS()
# sms_db.Test()
# sms_db.Insert(1, "+8615346665627", "123456", "sms-activate", getTime())
# li = sms_db.ListByDesc(100)
# for i in li:
#     print(i)
