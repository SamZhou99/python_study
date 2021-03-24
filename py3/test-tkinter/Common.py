class Style:
    @staticmethod
    def font():
        return ("Courier Prime", 32)

    @staticmethod
    def bg():
        return '#EEEEEE'

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')