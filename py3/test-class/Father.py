class Father(object):

    def __init__(self, name):
        self.name = name
        # print("Father name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name
