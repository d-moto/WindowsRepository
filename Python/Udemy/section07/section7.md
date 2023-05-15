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
toyota_car.run() # 継承元のメソッドrunを使用できる。

tesla_car = TeslaCar()
tesla_car.run() # 継承元のメソッドrunを使用できる。
tesla_car.auto_run() # 自身のメソッドももちろん使用できる。
```


## 82. メソッドのオーバーライドとsuperによる親のメソッドの呼び出し
以下のコードは同じ関数名がいくつか定義されているが、自身のクラスのものが優先されて呼び出される。（メソッドのオーバーライド）
```python
class Car(object):
    def run(self): # 同じ関数名が複数使用されている。
        print('run')

class ToyotaCar(Car):
    def run(self): # 同じ関数名が複数使用されている。
        print('toyota run')

class TeslaCar(Car):
    def run(self): # 同じ関数名が複数使用されている。
        print('tesla run')

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print("#################")
toyota_car = ToyotaCar()
toyota_car.run()

print("#################")
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
```

実行結果
```python
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
run
#################
toyota run
#################
tesla run
auto run

Process finished with exit code 0
```

```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self): # 同じ関数名が複数使用されている。
        print('run')

class ToyotaCar(Car):
    def run(self): # 同じ関数名が複数使用されている。
        print('toyota run')

class TeslaCar(Car):
    def run(self): # 同じ関数名が複数使用されている。
        print('tesla run')

    def auto_run(self):
        print('auto run')

print("####################")
normal_car = Car()
print(normal_car.model)

print("####################")
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model) # メソッド、クラスともに、「.」で呼び出せる。
toyota_car.run() # メソッド、クラスともに、「.」で呼び出せる。
```
実行結果
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
####################
None
####################
Lexus
toyota run

Process finished with exit code 0
```

以下のコードは、CarクラスとToyotaCarクラスどちらにも`__init__`があるので、★の部分のコードは同じことを2度書くことになる。
クラス継承した場合、Carの`__init__`をToyotaCarの`__init__`が上書きしてしまうので、同じことをもう一回書かないといけなくなる。
これを避けるには、
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model # ★

    def run(self): # 同じ関数名が複数使用されている。
        print('run')

class ToyotaCar(Car):
    def run(self): # 同じ関数名が複数使用されている。
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        self.model = model # ★
        self.enable_auto_run = enable_auto_run

    def run(self): # 同じ関数名が複数使用されている。
        print('tesla run')

    def auto_run(self):
        print('auto run')

print("####################")
normal_car = Car()
print(normal_car.model)

print("####################")
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model) # メソッド、クラスともに、「.」で呼び出せる。
toyota_car.run() # メソッド、クラスともに、「.」で呼び出せる。
```
↓
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model # ★

    def run(self): # 同じ関数名が複数使用されている。
        print('run')

class ToyotaCar(Car):
    def run(self): # 同じ関数名が複数使用されている。
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        ## self.model = model # ★
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self.enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。

    def run(self): # 同じ関数名が複数使用されている。
        print('tesla run')

    def auto_run(self):
        print('auto run')

print("####################")
normal_car = Car()
print(normal_car.model)

print("####################")
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model) # メソッド、クラスともに、「.」で呼び出せる。
toyota_car.run() # メソッド、クラスともに、「.」で呼び出せる。
```

## 83. プロパティを使った属性の設定
以下のコードは、TeslaCarクラスのオブジェクトにデフォルト引数で渡したenable_auto_run=Falseの値を出力している。
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):。
        print('run')

class ToyotaCar(Car):
    def run(self): 
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self.enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。

    def run(self): 
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar()
print(tesla_car.enable_auto_run)
```
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
False

Process finished with exit code 0
```
以下のようなコードで書き換えができてしまう。
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self.enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。

    def run(self):
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar()
tesla_car.enable_auto_run = True # ★ enable_auto_runにTrueを代入している。
print(tesla_car.enable_auto_run)
```
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
True

Process finished with exit code 0
```

勝手にオブジェクトを生成されて、enable_auto_runの値を書き換えられたくない場合にプロパティを使用する。
プロパティはクラス変数を定義する時に、その変数の頭にアンダースコアを付ける。
`self.enable_auto_run = enable_auto_run` -> `self._enable_auto_run = enable_auto_run`
※「_」付けたからと言って、プロパティなるわけではない。以下のようにアンスコを付けてもコードとしては動く。
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self._enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。

    def run(self):
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar()
tesla_car._enable_auto_run = True # ★ enable_auto_runにTrueを代入している。
print(tesla_car._enable_auto_run)
```
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
True

Process finished with exit code 0
```

enable_auto_run(self)メソッドを作成して、returnでself._enable_auto_runを返してやる。
enable_auto_run(self)メソッドの上には、デコレーターでプロパティであることを明示する。
以下のコードはエラーで終了する。
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self._enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。

    # このように書くことで、読み込みはできるけど、書き込みはできないという状況になる。telsa_car.enable_auto_runで値の取得はできるが、telsa_car.enable_auto_run = 'something'のように書き込みはできなくなる。
    # また、プロパティがつくと、呼び出す際に、()がいらない。`tesla_car.enable_auto_run()`ではなく、`tesla_car.enable_auto_run`で@property以下の関数が呼び出される。
    @property # デコレーター
    def enable_auto_run(self):
        return self._enable_auto_run
＠＠
    def run(self):
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar()
tesla_car.enable_auto_run = True # ★ enable_auto_runにTrueを代入している。
print(tesla_car.enable_auto_run)
```
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
Traceback (most recent call last):
  File "C:\Users\mokos\PycharmProjects\python_programming\lesson.py", line 73, in <module>
    tesla_car.enable_auto_run = True # ★ enable_auto_runにTrueを代入している。
AttributeError: can't set attribute

Process finished with exit code 1
```

書き換えを行いたいとき。
以下のようなコードで実現できる。
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self._enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。

    # このように書くことで、読み込みはできるけど、書き込みはできないという状況になる。telsa_car.enable_auto_runで値の取得はできるが、telsa_car.enable_auto_run = 'something'のように書き込みはできなくなる。
    # また、プロパティがつくと、呼び出す際に、()がいらない。`tesla_car.enable_auto_run()`ではなく、`tesla_car.enable_auto_run`で@property以下の関数が呼び出される。
    @property # デコレーター
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter # @propertyで指定した関数名(enable_auto_run).setterという命名規則がある。
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

    def run(self):
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar()
tesla_car.enable_auto_run = True # ★ @enable_auto_run.setterのis_enable変数にTrueを代入している。そのあとに、self._enable_auto_runにis_enableの値（True）が代入されている。
print(tesla_car.enable_auto_run)
```
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
True

Process finished with exit code 0
```

上記のようなコードを書く時、ある条件に合致した時だけ、プロパティを書き換える、というような書き方をすることが多い。
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False, passwd='123'):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self._enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。
        self.passwd = passwd # init関数で、passwdを設定する。

    # このように書くことで、読み込みはできるけど、書き込みはできないという状況になる。telsa_car.enable_auto_runで値の取得はできるが、telsa_car.enable_auto_run = 'something'のように書き込みはできなくなる。
    # また、プロパティがつくと、呼び出す際に、()がいらない。`tesla_car.enable_auto_run()`ではなく、`tesla_car.enable_auto_run`で@property以下の関数が呼び出される。
    @property # デコレーター
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456': # パスワードが456に一致した場合のみ、プロパティの書き換えを可能とする。
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('tesla run')

    def auto_run(self):
        print('auto run')

# プロパティの書き換え成功。
print('#################################')
tesla_car = TeslaCar(passwd='456')
tesla_car.enable_auto_run = True # ★ enable_auto_runにTrueを代入している。（enable_auto_run()が呼ばれ、is_enableにTrueを代入しようとする。
print(tesla_car.enable_auto_run)

# プロパティの書き換え失敗。
print('#################################')
tesla_car = TeslaCar()
tesla_car.enable_auto_run = True # ★ enable_auto_runにTrueを代入している。（enable_auto_run()が呼ばれ、is_enableにTrueを代入しようとする。
print(tesla_car.enable_auto_run)
```

```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False, passwd='123'):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self._enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。
        self.passwd = passwd # init関数で、passwdを設定する。

    # このように書くことで、読み込みはできるけど、書き込みはできないという状況になる。telsa_car.enable_auto_runで値の取得はできるが、telsa_car.enable_auto_run = 'something'のように書き込みはできなくなる。
    # また、プロパティがつくと、呼び出す際に、()がいらない。`tesla_car.enable_auto_run()`ではなく、`tesla_car.enable_auto_run`で@property以下の関数が呼び出される。
    @property # デコレーター
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456': # パスワードが456に一致した場合のみ、プロパティの書き換えを可能とする。
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar(passwd='456')
print(tesla_car._enable_auto_run) # TeslaCarクラスのself._enable_auto_runを直接参照している。
```
↑TeslaCarクラスのself._enable_auto_runを直接参照している。
これを完全に隠す場合。self.__enable_auto_runという具合に、アンスコを2つ書く。
`print(tesla_car.__enable_auto_run)`ではエラーが出るようになる。
↓
```python
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('toyota run')

class TeslaCar(Car):
    def __init__(self, model ='Model S', enable_auto_run=False, passwd='123'):
        super().__init__(model) # `super().__init__(model)`と書くことで、Carの`__init__`を呼び出せる。ToyotaCarの`__init__`の中で、Carの`__init__`を呼び出すことが出きる。
        self.__enable_auto_run = enable_auto_run # 呼び出してから、TeslaCarだけの`__init__`で実行したい記述を書く。
        self.passwd = passwd # init関数で、passwdを設定する。

    # このように書くことで、読み込みはできるけど、書き込みはできないという状況になる。telsa_car.enable_auto_runで値の取得はできるが、telsa_car.enable_auto_run = 'something'のように書き込みはできなくなる。
    # また、プロパティがつくと、呼び出す際に、()がいらない。`tesla_car.enable_auto_run()`ではなく、`tesla_car.enable_auto_run`で@property以下の関数が呼び出される。
    @property # デコレーター
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456': # パスワードが456に一致した場合のみ、プロパティの書き換えを可能とする。
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print(self.__enable_auto_run) # `__enable_auto_run`はクラス外からはアクセスできないが、クラスないなら、アクセスできる。
        print('tesla run')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar(passwd='456')
print(tesla_car.__enable_auto_run) 
```
```
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
Traceback (most recent call last):
  File "C:\Users\mokos\PycharmProjects\python_programming\lesson.py", line 83, in <module>
    print(tesla_car.__enable_auto_run)
AttributeError: 'TeslaCar' object has no attribute '__enable_auto_run'

Process finished with exit code 1C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
Traceback (most recent call last):
  File "C:\Users\mokos\PycharmProjects\python_programming\lesson.py", line 83, in <module>
    print(tesla_car.__enable_auto_run)
AttributeError: 'TeslaCar' object has no attribute '__enable_auto_run'

Process finished with exit code 1
```


練習
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

以下のように、クラスは構造体のように扱う事ができる。
クラスでは定義していない変数`t.name`,`t.age=`を定義できてしまう。
```python
class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name)
```

プロパティを書き換えることができてしまう。
```python
class T(object):
    
    def __init__(self, proper='INIT PARAM'):
        self.__proper = proper

    @property
    def proper(self):
        return self.__proper

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)
t.__proper = 'XXXXXXXXXXXXX' # 新しく、__properを作成してしまう。
print(t.__proper)
print(t.proper)
```
```python
C:\Users\mokos\anaconda3\python.exe C:\Users\mokos\PycharmProjects\python_programming\lesson.py 
Mike 20
XXXXXXXXXXXXX
INIT PARAM

Process finished with exit code 0
```

## 85. ダックタイピング

```python
class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('drive ok')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)
car.ride(baby)
```

## 86. 抽象クラス
## 87. 多重継承
## 88. クラス変数
## 89. クラスメソッドとスタティックメソッド
## 90. 特殊メソッド
