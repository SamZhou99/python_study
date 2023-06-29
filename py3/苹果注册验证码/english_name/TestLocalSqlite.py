from LocalSqlite import LocalSqlite
from FullEnglishName import FullEnglishName


def testSqlite():
    db = LocalSqlite()
    # res = db.Test()
    # res = db.Insert(1, "aaa", "en")
    # res = db.Update(1, 1)
    # res = db.List(100)
    # for i in res:
    #     print(i)

    # words = "abcdefghijklmnopqrstuvwxyz"
    # for i in range(len(words)):
    #     res = db.Insert(1, words[i], "en")

    res = db.FindRandom()
    for obj in res:
        print(obj)
        # db.Update(obj["id"], 0)

    # res = db.Count()
    # for obj in res:
    #     print(obj)
    #     if obj["total"] == 0:
    #         db.UpdateAllStatus()
    db.Close()


def add_row(word, type):
    db = LocalSqlite()
    return db.Insert(1, word, type)


def add():
    db = LocalSqlite()
    return db.Insert(1, "Sam", "english")


def init():
    # testSqlite()
    n = FullEnglishName()
    name = n.FillName()
    print(name)


init()
