## 78. クラスの定義
```python
# section7.py
# classの使用例
# キャピタライズ（最初の文字を大文字に）
s = 'apple'
print(s.capitalize())

# classを作成
class Person(object):
    def say_something(self):
        print('HELLO!')

# classを呼び出す,person変数にPersonクラスを代入
person = Person()

# Personクラスのメソッドを使用する
person.say_something()

# 例えば関数を作成して、書くこともできるが、これはオブジェクト指向とはならない。
def personA(name):
    if name=='A':
        print('hey A!')
```

pyCharmだと、[Go To]->[Declaration]でクラス情報などが見れる
```python
class str(object): 
def capitalize となっている
```
```python
s = 'apple'
S = s.capitalize() ここがクラスのメソッドを使用してる箇所。string型のクラスにはcapitalizeというメソッドが用意されている
print(S)
```

python3であれば、
```python
class Person: または class Person()
    def say_something(self):
        print('HELLO')
```
と書くこともできるがobjectは書いたほうがいい。クラス継承とかもあるため

## 79. クラスの初期化とクラス変数
     
クラスの初期化。クラスのオブジェクトが作成された段階で、__init__関数は呼び出される。  
person = Person()とオブジェクトを作成した時点で、print('First')が実行される。
```python
class Person(object):
    def __init__(self):
        print('First')

    def say_something(self):
        print('hello')

person = Person()
```

値を保持したい時は、(self, name)のようにして、メソッドを作成する。
```python
class Person(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_something(self):
        # ほかのメソッドからもself.nameは呼び出せる。
        print('I am {}. hello'.format(self.name))
        # ほかのメソッドからほかのメソッドも呼び出せる。
        self.run(10)

    def run(self, num):
        print('run' * num)

person = Person('Mike')
```

## 80. コンストラクタとデストラクタ
`__init__(self)`が実はコンストラクタ  
コンストラクタはオブジェクトが作成された時点で実行される。  
`__del__(self)`がデストラクタ  
デストラクタはオブジェクトがなくなるときに実行される。  
```python
class Person(object):
    def __init__(self):
        print('First')

    def say_something(self):
        print('hello')

    def __del__(self):
        print('good bye')

person = Person()
print('#########')
```
上記を実行すると、以下のようになる。
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson7.py 
First
#########
good bye

Process finished with exit code 0
```

デストラクタを明示的に呼びたい時
```python
class Person(object):
    def __init__(self):
        print('First')

    def say_something(self):
        print('hello')

    def __del__(self):
        print('good bye')

person = Person()
del person ## del で消す。
print('#########')
```
上記を実行した結果
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson7.py 
First
good bye
#########

Process finished with exit code 0
```

## 81. クラスの継承
```python
class Car(object):
    pass # passは何もしないという意味。

class ToyotaCar(Car): # ToyotaCar()クラスにCarクラスを継承した。
    pass # passは何もしないという意味。
```

クラスの継承は、元のクラスの機能を引き継いで、拡張するというようなイメージ

```python
class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
```


## 82. メソッドのオーバーライドとsuperによる親のメソッドの呼び出し
```python
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
```

実行結果
```
(base) C:\Users\mokos\Git_work>C:/Users/mokos/anaconda3/python.exe c:/Users/mokos/Git_work/Python/Udemy/section07/section7-2.py

INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 12, 12
color : red
INFO : call super get_info
INFO : excuted get_info
bottom : 12
height : 12
INFO : excuted cal_area
area : 72.0
area : 72.0

INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 12, 12
color : black
INFO : call super get_info
INFO : excuted get_info
bottom : 12
height : 12
INFO : excuted cal_area
area : 72.0
area : 72.0

INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 10, 30
color : black
INFO : call super get_info
INFO : excuted get_info
bottom : 10
height : 30
INFO : excuted cal_area
area : 150.0
area : 150.0

INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 12, 10
color : green
INFO : call super get_info
INFO : excuted get_info
bottom : 12
height : 10
INFO : excuted cal_area
area : 60.0
area : 60.0

INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 12, 12
color : black
INFO : call super get_info
INFO : excuted get_info
bottom : 12
height : 12
INFO : excuted cal_area
area : 72.0
area : 72.0
False
INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 12, 12
color : black
INFO : call super get_info
INFO : excuted get_info
bottom : 12
height : 12
INFO : excuted cal_area
area : 72.0
area : 72.0
True
INFO : call super init
INFO : excuted init
INFO : excuted TriangleColor init
INFO : call super set_param
INFO : excuted set_param
set param : 12, 12
color : black
INFO : call super get_info
INFO : excuted get_info
bottom : 12
height : 12
INFO : excuted cal_area
area : 72.0
area : 72.0
Traceback (most recent call last):
  File "c:\Users\mokos\Git_work\Python\Udemy\section07\section7-2.py", line 80, in <module>
    tricol7.flag = True
  File "c:\Users\mokos\Git_work\Python\Udemy\section07\section7-2.py", line 57, in flag
    raise ValueError
ValueError
INFO : excuted del
INFO : excuted del
INFO : excuted del
INFO : excuted del
INFO : excuted del
INFO : excuted del
INFO : excuted del

(base) C:\Users\mokos\Git_work>
```

## 84. クラスを構造体として扱うときの注意点
## 85. ダックタイピング
## 86. 抽象クラス
## 87. 多重継承
## 88. クラス変数
## 89. クラスメソッドとスタティックメソッド
## 90. 特殊メソッド
