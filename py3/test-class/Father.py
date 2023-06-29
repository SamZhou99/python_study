class Father(object):
    def __init__(self, name):
        self.fatherName = name
        # print("Father name: %s" % (self.name))

    def __str__(self) -> str:
        return self.fatherName

    def getFatherName(self):
        return "爸爸 " + self.fatherName
