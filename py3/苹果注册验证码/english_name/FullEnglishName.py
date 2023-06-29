from english_name.LocalSqlite import LocalSqlite


class FullEnglishName:
    def __init__(self) -> None:
        pass

    def FillName(self):
        db = LocalSqlite()
        res = db.FindRandom()
        for obj in res:
            first_name = obj["word"]
            db.Update(obj["id"], 0)

        res = db.FindRandomLastName()
        for obj in res:
            last_name = obj["word"]

        return first_name, last_name
