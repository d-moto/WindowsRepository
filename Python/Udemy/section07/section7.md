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
## 83. プロパティーを使った属性の設定
## 84. クラスを構造体として扱うときの注意点
## 85. ダックタイピング
## 86. 抽象クラス
## 87. 多重継承
## 88. クラス変数
## 89. クラスメソッドとスタティックメソッド
## 90. 特殊メソッド
