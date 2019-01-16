from Father import Father


class Son(Father):

    def __init__(self, name):
        super(Son, self).__init__('Lven')
        self.name2 = name

    def getParentName(self):
    	return super(Son, self).getName()

    def getName(self):
        return 'Son ' + self.name2
