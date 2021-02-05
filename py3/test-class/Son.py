from Father import Father


class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__('Sam')
        self.sonName = name

    def getParentName(self):
        return super(Son, self).getFatherName()

    def getName(self):
        return '儿子 ' + self.sonName
