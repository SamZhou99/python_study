import os


class MailboxName:
    def __init__(self) -> None:
        self.PATH = os.getcwd()
        self.INDEX_TXT_PATH = "{}/web_email_api/mail_index.txt".format(self.PATH)
        self.EMAIL_TXT_PATH = "{}/web_email_api/mail_format.txt".format(self.PATH)
        self.INDEX = self._readEMailIndex()
        self.EMAIL_LIST = self._readEmailText()

    def getName(self):
        name = self.EMAIL_LIST[self.INDEX]
        self.INDEX += 1
        self._writeEMailIndex(self.INDEX)
        return name

    def _readEMailIndex(self):
        f = open(self.INDEX_TXT_PATH, "r")
        t = f.read()
        return int(t)

    def _readEmailText(self):
        f = open(self.EMAIL_TXT_PATH, "r")
        t = f.read()
        a = t.split("\n")
        l = []
        for i in a:
            email = i.split("|")[1]
            l.append(email)
        return l

    def _writeEMailIndex(self, index):
        f = open(self.INDEX_TXT_PATH, "w")
        f.write(str(index))
        return True
