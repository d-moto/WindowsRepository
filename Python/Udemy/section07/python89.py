class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod # 引数にはselfなどはいらない。クラス、オブジェクトのメソッドとして機能しない。（クラスの外に書いても良い。ただ、コードの可読性を考えると中にかけると便利という話）
    def about():
        print('about human')


a = Person()
print(a.what_is_your_kind())

b = Person
print(b.what_is_your_kind())

print(Person.kind)
print(Person.what_is_your_kind())

Person.about()