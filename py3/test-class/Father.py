class Father(object):

    def __init__(self, name):
        self.fatherName = name
        # print("Father name: %s" % (self.name))

    def getFatherName(self):
        return '爸爸 ' + self.fatherName
