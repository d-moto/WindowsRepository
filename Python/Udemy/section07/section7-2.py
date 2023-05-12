class Triangle(object):
    def __init__(self):
        print('INFO : excuted init')

    def set_param(self, bottom, height):
        self.bo = bottom
        self.he = height
        print('INFO : excuted set_param')
        print(f'set param : {self.bo}, {self.he}')

    def get_param(self):
        print('INFO : excuted get_param')
        print(f'bottom : {self.bo}')
        print(f'height : {self.he}')

    def cal_area(self):
        print('INFO : excuted cal_area')
        area = self.bo * self.he / 2
        print(f'area : {area}')
        return area

    def get_info(self):
        print('INFO : excuted get_info')
        print(f'bottom : {self.bo}')
        print(f'height : {self.he}')
        # クラス内のメソッドから、同じクラス内のメソッドが呼び出せるみたい。
        tmp_area = Triangle.cal_area(self)
        print(f'area : {tmp_area}')

    def __del__(self):
        print('INFO : excuted del')

## Triangleクラスの継承
class TriangleColor(Triangle):
    def __init__(self, color='black', bottom=12, height=12, pw='', flag=False):
        self.co = color
        self.pw = pw
        self._flag = flag
        print('INFO : call super init')
        super().__init__()
        print('INFO : excuted TriangleColor init')
        print('INFO : call super set_param')
        super().set_param(bottom, height)
        print(f'color : {self.co}')
        print('INFO : call super get_info')
        super().get_info()
    
    @property
    def flag(self):
        return self._flag
    
    @flag.setter
    def flag(self, is_enable):
        if self.pw == 123:
            self._flag = is_enable
        else:
            raise ValueError

print('')
tricol1 = TriangleColor('red')
print('')
tricol2 = TriangleColor()
print('')
tricol3 = TriangleColor(bottom=10, height=30)
print('')
tricol4 = TriangleColor(color='green', height=10)
print('')

# プロパティの確認
tricol5 = TriangleColor()
print(tricol5.flag)

# プロパティの書き換え
tricol6 = TriangleColor(pw=123)
tricol6.flag = True
print(tricol6.flag)

# プロパティの書き換え失敗
tricol7 = TriangleColor(pw=111)
tricol7.flag = True
print(tricol7.flag)
