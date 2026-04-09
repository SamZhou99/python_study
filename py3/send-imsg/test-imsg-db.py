import ModulePlistlib
from ClassSqlite import ClassSqlite

DBPath = "/Users/sam/Library/Messages/chat.db"
SQLite = ClassSqlite(DBPath)


def show_chat(chat_id, msg_id):
    sql = "SELECT ROWID,properties FROM chat WHERE ROWID={}".format(chat_id)
    res = SQLite.select(sql)
    for item in res:
        res_properties = ModulePlistlib.parseImessageText(item["properties"])
        print("🎃chat：", chat_id, res_properties)


def show_message(chat_id, msg_id):
    sql = "SELECT ROWID,text,attributedBody,error FROM message WHERE ROWID={}".format(
        msg_id
    )
    res = SQLite.select(sql)
    for item in res:
        text = item["text"]
        attributedBody = ModulePlistlib.parseImessageText(item["attributedBody"])
        print(
            "   🎃message：",
            chat_id,
            msg_id,
            "error:",
            item["error"],
            text or attributedBody,
        )


def show_message_by_phone(phone):
    sql = "SELECT * FROM chat WHERE chat_identifier='{}'".format(phone)
    res = SQLite.select(sql)
    item = res[0]
    print(
        "🥶chat：",
        item["ROWID"],
        item["state"],
        item["chat_identifier"],
        item["service_name"],
        item["successful_query"],
    )

    sql = "SELECT * FROM chat_message_join WHERE chat_id='{}'".format(item["ROWID"])
    res = SQLite.select(sql)
    for item in res:
        chat_id, msg_id = item["chat_id"], item["message_id"]
        show_message(chat_id, msg_id)
    print("\n")


def init():
    sql = "SELECT * FROM chat WHERE state=3 AND service_name='iMessage' AND successful_query=1 ORDER BY ROWID DESC LIMIT 20"
    res = SQLite.select(sql)
    for item in res:
        show_message_by_phone(item["chat_identifier"])

    SQLite.finish()
    print("执行完成")


init()
