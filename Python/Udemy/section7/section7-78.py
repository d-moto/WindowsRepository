# classの使用例
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
    else:
        print('never')

personA('Taro')
personA('A')


