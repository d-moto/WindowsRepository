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
## 80. コンストラクタとデストラクタ
## 81. クラスの継承
## 82. メソッドのオーバーライドとsuperによる親のメソッドの呼び出し
## 83. プロパティーを使った属性の設定
## 84. クラスを構造体として扱うときの注意点
## 85. ダックタイピング
## 86. 抽象クラス
## 87. 多重継承
## 88. クラス変数
## 89. クラスメソッドとスタティックメソッド
## 90. 特殊メソッド
