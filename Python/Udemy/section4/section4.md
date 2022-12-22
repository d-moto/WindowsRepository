# データ構造

## リスト型
```python
>>> l = [1, 20, 4, 2, 45, 2, 11]
>>> l
[1, 20, 4, 2, 45, 2, 11]
>>> print(l)
[1, 20, 4, 2, 45, 2, 11]
>>> print(l[0])
1
>>> print(l[1]) 
20
>>> print(l[4]) 
45
>>> print(l[-1]) 
11
>>> print(l[-2]) 
2
>>> print(l[-3]) 
45
>>> print(l[0:3]) 
[1, 20, 4]
>>> print(l[2:7]) 
[4, 2, 45, 2, 11]
>>>
>>> print(l[2:])  
[4, 2, 45, 2, 11]
>>> print(l[:])  
[1, 20, 4, 2, 45, 2, 11]
>>>

>>> l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index0 から index3の1つ手前までを表示。
>>> print(l[0:3])
[0, 1, 2]
>>> print(l[1:3])
# index1 から index3の1つ手前までを表示。 
[1, 2]
>>> 
# index1 から index9の1つ手前までを表示。
>>> print(l[1:9]) 
[1, 2, 3, 4, 5, 6, 7, 8]

# index2 から index9の1つ手前までを表示。
>>> print(l[2:9]) 
[2, 3, 4, 5, 6, 7, 8]
>>>

>>> len(l)
7
>>> type(l)
<class 'list'>
>>>
>>> list('abcdefg')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n[::]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n[::2] 
[1, 3, 5, 7, 9]
>>> n[::-1] 
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>>

>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>>
>>> x[0]
['a', 'b', 'c']
>>> x[1]
[1, 2, 3]
>>> x[0][1]
'b'
>>> x[0][0]
'a'
>>> x[1][1]
2
>>>
```

## リストの操作
```python
>>> s = ['a' 'b' 'c' 'd' 'e' 'f' 'g']
>>> s
['abcdefg']
>>>
>>> s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[0]
'a'
>>> s[0] = 'X'
>>> s
['X', 'b', 'c', 'd', 'e', 'f', 'g']
>>> s[2:5]
['c', 'd', 'e']
>>> s[2:5] = ['C', 'D', 'E']
>>> s
['X', 'b', 'C', 'D', 'E', 'f', 'g']
>>> s[2:5] = []
>>> s
['X', 'b', 'f', 'g']
>>> s[:]
['X', 'b', 'f', 'g']
>>> s[:] = []
>>> s
[]
>>>

>>> n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
>>> n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
>>> n.append(100)
>>> n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 100]
>>> n.insert(0,200)
>>> n
[200, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 100]
>>> n.insert(1,500)
>>> n
[200, 500, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 100]
>>> n.pop()
100
>>> n.pop(0)
200
>>> n[2:11]
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> n[2:12]
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
>>> n[2:12] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n
[200, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n.pop()
10
>>> n
[200, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> n.append(10)
>>> n
[200, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> n.append(100)
>>> n
[200, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
>>> del n[0]
>>> n
[500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
>>> del n
>>> n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
>>> n = [1, 2, 2, 2, 3]
>>> n
[1, 2, 2, 2, 3]
>>> n.remove(2)
>>> n
[1, 2, 2, 3]
>>> n.remove(2)
>>> n
[1, 2, 3]
>>> n.remove(2)
>>> n
[1, 3]
>>> n.remove(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>>
>>> a = [1, 2, 3, 4, 5]
>>> b = [6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5]
>>> b
[6, 7, 8, 9, 10]
>>> x = a + b
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a
[1, 2, 3, 4, 5]
>>> b
[6, 7, 8, 9, 10]
>>> a += b
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [1, 2, 3, 4, 5]
>>> y = [6, 7, 8, 9, 10]
>>> x.extend(y)
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>


```
## リストのメソッド
```python
# リストの定義
r = [1, 2, 3, 4, 5, 1, 2, 3]

# 要素3がどのindexか調べる。初めにヒットしたものしか出力しない。
print(r.index(3))

# 要素3のサーチを4番目のindexから始める場合。
print(r.index(3, 4))

# 要素の数を数える場合。
print(r.count(3))

# rに5が入っているかどうか。
if 5 in r:
    print('exist')

# リストのソート
r.sort()
print(r)

# リストのソート（リバース）
r.sort(reverse=True)
print(r)

# リストのソート（リバース２）
r.reverse()
print(r)

# スプリット
# s.split(' ')で空白を基準にリストに格納してくれる。
s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

# もとに戻す
x = ' '.join(to_split)
print(x)

# helpの表示
print(help(list))
```

## リストのコピー
```python
## リストのコピー

# iにもjにも100が挿入されてしまう。
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

# リストのコピーは以下のようにする
# x = y とすると、yには、xのリストのアドレスがyに格納される（参照わたし）
x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:] とすることでもy = x.copy()と同様のことができるが、見にくいのであまりやらない。
y[0] = 100
print('y =', y)
print('x =', x)

X = 20
Y = X
Y = 5
print('X : ', id(X))
print('Y : ', id(Y))

X = [ 'a', 'b' ]
Y = X
Y[0] = 'p'
# まったく同じIDが出力される。
print('X : ', id(X))
print('Y : ', id(Y))
```

## リストの使いどころ
```python
seat = []
min = 0
max = 5
min <= len(seat) < max

seat.append('p')
min <= len(seat) < max
len(seat)

seat.append('p')
min <= len(seat) < max
len(seat)

seat.append('p')
min <= len(seat) < max
len(seat)

seat.append('p')
min <= len(seat) < max
len(seat)

seat.append('p')
min <= len(seat) < max
len(seat)

```

## タプル型
```python
# タプルは（）で括り、宣言する。
>>> t = (1, 2, 3, 4, 1, 2)
>>> t
(1, 2, 3, 4, 1, 2)
>>>
>>> type(t)
<class 'tuple'>
>>> t[0]
1

# タプルは一度宣言すると、要素の値を変更することはできない。
# 変更しようとすると以下のようなエラーとなる。
>>> t[0] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>

# リストと同様に、インデックスを指定して値を参照することができる。
>>> t[-2]
1
>>> t[2:]
(3, 4, 1, 2)
>>> t.index(1)
0
>>> t.index(1, 1)
4

# ヘルプを見るとわかるが、値を変更できないという性質上、タプルを操作するメソッドは、リストほど多くはない。
>>> help(tuple)
Help on class tuple in module builtins:

class tuple(object)
 |  tuple(iterable=(), /)
 |
 |  Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
 |  If the argument is a tuple, the return value is the same object.
 |
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>>
>>>

# タプルの要素にリストを入れることは可能。
>>> t = ([1, 2, 3], [4, 5, 6])
>>> t
([1, 2, 3], [4, 5, 6])
>>> t[0]
[1, 2, 3]

# タプル内の、リストの要素は変更可能。
>>> t[0][0]
1
>>> t[0][0] = 100
>>> t
([100, 2, 3], [4, 5, 6])
>>>

# 以下のような表現でもタプルは宣言可能。
>>> t = 1, 2, 3
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 3)
>>>

# 要素が1つしかないタプルの場合、要素の後に「,」が必要。
>>> t = 1,
>>> type(t)
<class 'tuple'>
>>>
>>> t
(1,)
>>>
>>> t = ()
>>> type(t)
<class 'tuple'>
>>> t
()
>>>

# コンマがないと、タプルとはならない。
>>> t = (1)
>>> t
1
>>> type(t)
<class 'int'>
>>> t
1
>>>
>>> t = ('test')
>>> type(t)
<class 'str'>
>>> t = ('test',)
>>> type(t)
<class 'tuple'>
>>>
>>> t = 1,
>>> t + 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "int") to tuple
>>>
>>> new_tuple = (1, 2, 3) + (4, 5, 6)
>>> new_tuple
(1, 2, 3, 4, 5, 6)
>>> new_tuple = (1, 2, 3) + (4, 5, 6)
>>> new_tuple = (1) + (4, 5, 6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>>
>>> new_tuple = (1,) + (4, 5, 6)
>>> new_tuple
(1, 4, 5, 6)
>>>

```

## タプルのアンパッキング
```python
# tupleのアンパッキング
num_tuple = (10, 20)
print(num_tuple)

# タプルがアンパッキングされ、要素がそれぞれx,yに格納される。
x, y = num_tuple
print(x, y)

x, y = (10, 20)
x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100 
b = 200
print(a, b)

a, b = b, a
print(a, b)
```

## タプルの使いどころ
```python
chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)
```

## 辞書型
```python
>>> d = {'x': 10, 'y': 20}
>>> d
{'x': 10, 'y': 20}
>>> type(d)
<class 'dict'>
>>> d['x']
10
>>> d['y']
20
>>> d['x'] = 100
>>>
>>> d
{'x': 100, 'y': 20}
>>> d['x'] = 'XXXX'
>>> d
{'x': 'XXXX', 'y': 20}
>>>
>>> d['z'] = 4000
>>> d
{'x': 'XXXX', 'y': 20, 'z': 4000}
>>> d[1] = 10000
>>> d
{'x': 'XXXX', 'y': 20, 'z': 4000, 1: 10000}
>>> dict(a=10, b=20)
{'a': 10, 'b': 20}
>>> dict([('a', 10), ('b', 40)])
{'a': 10, 'b': 40}
>>>
```


## 辞書型のメソッド
```python
>>> d = {'x': 10, 'y': 20}
>>> help(d)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |
 |  Methods defined here:
 |
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __ior__(self, value, /)
 |      Return self|=value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |
 |      If key is not found, default is returned if given, otherwise KeyError is raised
 |
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

>>> d.keys()
dict_keys(['x', 'y'])
>>> d.values()
dict_values([10, 20])
>>> d2 = {'x': 1000, 'j': 500}
>>>
>>> d
{'x': 10, 'y': 20}
>>> d2
{'x': 1000, 'j': 500}
>>>
>>> d.update(d2)
>>> d
{'x': 1000, 'y': 20, 'j': 500}
>>>
>>> d['x']
1000
>>> d.get('x')
1000
>>> d['z']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'
>>> d.get('z')
>>> r = d.get('z')
>>> r
>>> type(r)
<class 'NoneType'>
>>>
>>> d
{'x': 1000, 'y': 20, 'j': 500}
>>> d.get('x')
1000
>>> d
{'x': 1000, 'y': 20, 'j': 500}
>>>
>>> d.pop('x')
1000
>>> d
{'y': 20, 'j': 500}
>>> del d['y']
>>> d
{'j': 500}
>>> del d
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>>
>>> d = {'a': 100, 'b': 200}
>>> d.clear()
>>> d
{}
>>>
>>> d = {'a': 100, 'b': 200}
>>> d
{'a': 100, 'b': 200}
>>>
>>> 'a' in d
True
>>> 'j' in d
False
>>>
```


## 辞書のコピー
```python
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
```

## 辞書の使いどころ
```python
fruits = {
  'apple': 100,
  'banana': 200,
  'orange': 300,
}

print(fruits['apple'])


l = [
  ['apple', 100 ],
  ['banana', 200 ],
  ['orange', 300 ],
]


```

## 集合型
```python
>>> a = {1, 2, 3, 4, 4, 4, 4, 6, 4}
>>> a
{1, 2, 3, 4, 6}
>>> type(a)
<class 'set'>
>>>
>>> b = {2, 3, 3, 6, 7}
>>> b
{2, 3, 6, 7}
>>>
>>> a
{1, 2, 3, 4, 6}
>>> b
{2, 3, 6, 7}
>>> a - b
{1, 4}
>>>
>>> b - a
{7}
>>>
>>> a & b
{2, 3, 6}
>>> a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>>
>>> a | b
{1, 2, 3, 4, 6, 7}

# 排他的論理和
>>> a ^ b
{1, 4, 7}
>>>
```


## 集合のメソッド
```
>>> s = {1, 2, 3, 4, 5}
>>> s
{1, 2, 3, 4, 5}
>>>
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>>
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>>
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>>
>>> s.remove(6)
>>> s
{1, 2, 3, 4, 5}
>>>
>>> s.clear()
>>> s
set()
>>> a = {}
>>> type(a)
<class 'dict'>
>>> a
{}
>>>
>>> s
set()
>>> type(s)
<class 'set'>
>>>
>>> help(set)
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |
 |  Build an unordered collection of unique elements.
 |
 |  Methods defined here:
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iand__(self, value, /)
 |      Return self&=value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __ior__(self, value, /)
 |      Return self|=value.
 |
 |  __isub__(self, value, /)
 |      Return self-=value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __ixor__(self, value, /)
 |      Return self^=value.
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __reduce__(...)
 |      Return state information for pickling.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  add(...)
 |      Add an element to a set.
 |
 |      This has no effect if the element is already present.
 |
 |  clear(...)
 |      Remove all elements from this set.
 |
 |  copy(...)
 |      Return a shallow copy of a set.
 |
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |
 |      (i.e. all elements that are in this set but not the others.)
 |
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |
 |      If the element is not a member, do nothing.
 |
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |
 |      (i.e. all elements that are in both sets.)
 |
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |
 |  issubset(...)
 |      Report whether another set contains this set.
 |
 |  issuperset(...)
 |      Report whether this set contains another set.
 |
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |
 |      If the element is not a member, raise a KeyError.
 |
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |
 |      (i.e. all elements that are in exactly one of the sets.)
 |
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |
 |  union(...)
 |      Return the union of sets as a new set.
 |
 |      (i.e. all elements that are in either set.)
 |
 |  update(...)
 |      Update a set with the union of itself and others.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

>>>
>>>
```

## 集合の使いどころ
```python
my_friends = {'A', 'D', 'C'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)
```