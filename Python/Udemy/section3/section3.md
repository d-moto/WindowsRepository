# Pythonの基本 8_15

## 8. 変数宣言

</br>

- **変数宣言**
</br>
pythonでは、int,srtなど変数の宣言時に指定する必要はない。  
変数のタイプはtype()関数で確認できる。  
  ```python
  num = 1
  name = 'Mike'
  is_ok = True

  print(num, type(num))
  print(name, type(name))
  print(is_ok, type(is_ok))
  ```
  ↓ 実行結果
  ```python
  1 <class 'int'>
  Mike <class 'str'>
  True <class 'bool'>
  ```

- **型の上書きと型変換**
</br>
以下のようにすると、変数の上書きと、型変換ができる
  ```python
  # 型の上書き
  num = 1
  name = 'Mike'

  num = name

  print(num, type(num))
  ```
  ↓ 実行結果
  ```python
  Mike <class 'str'>
  ```
  ```python
  # 型の変換
  name = '1'

  new_num = int(name)

  print(new_num, type(new_num))
  ```
  ↓ 実行結果
  ```python
  1 <class 'int'>
  ```

- **型の宣言**  
一応Python3.9から型の宣言ができる
  ```python
  num: int = 1
  name: str = 'Mike'
  ```
  ただ基本的に使用しない。

- **変数の命名**  
Pythonでは、変数の先頭に数字は使用できない。
また、予約語も変数の名前には使用できない。

</br>

## 9. printで出力
</br>

- sep : 引数と引数の間の文字を設定する。（デフォルトではスペース）
- end : プリントの末尾の設定をする。（デフォルトでは改行[\n]）
```python
print('1', 'Hi')
print('2', 'Hi', 'Mike')
print('3', 'Hi', 'Mike', sep=',')
print('4', 'Hi', 'Mike', sep=',', end='.\n')

1 Hi
2 Hi Mike
3,Hi,Mike
4,Hi,Mike.
```

## 10. 数値
</br>

```python
## 数値の扱い
>>> 2 + 2 
4
>>> 5 - 2 
3
>>> 5 * 6
30
>>> 50 - 5 * 6
20
>>> (50 - 5) * 6
270
>>> 8/5
1.6
>>> type(1)
<class 'int'>
>>> type(1.6)
<class 'float'>
>>>
>>> 0.6
0.6
>>> .6
0.6
>>> 17/3
5.666666666666667
>>> 17 // 3
5
>>> 17 % 3
2
>>> 5 * 5
25
>>> 5 ** 5
3125
>>> 5 * 5 * 5 * 5 * 5
3125
>>> x = 5
>>> x
5
>>> y = 10
>>> x * y
50
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> pie = 3.1415151515151515 
>>> pie
3.1415151515151516
>>> round(pie, 2)
3.14
>>>

## 数学関数
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

## ドキュメントの表示
print(help(math))

```

## 11. 文字列
```python
# シングルクォート、ダブルクォーテーションどちらでも可。
print('hello')
print("hello")

# ダブルクォーテーション内にシングルクォートがあっても文字列として表示してくれる。
print("I don't know")

# シングルクォートを文字として表示したい時に以下のようにするとエラーがでる。
# print('I don't know')

# シングルクォートを文字列として表示したい場合は以下のようにバックスラッシュを入れる。（円マーク）
print('I don\'t know')

# シングルクォート内にダブルクォーテーションがあるのは可。
print('say "I don\'t know"')

# すべてをダブルクォーテーションで書くならば、以下のようにする。
print("say \"I don't know\"")

# 改行は、バックスラッシュとn（\n）
print('hello.\nHow are you?')

# winndowsのパスのようなもので、バックスラッシュの次にnがくると、予期せぬ結果になる。
print('C:\name\name')

# すべてを文字列として表示したい場合は、rawを意味するrを最初に書く。
print(r'C:\name\name')

# 以下のようにすると、改行を自動で行ってくれる。（「"""」ダブルクォーテーションを3つつなげる。）
print("######################")
print("""
line1
line2
line3
""")
print("######################")

# ただ上下に空白行ができるので、防ぎたい場合は、バックスラッシュを入れる
print("######################")
print("""\
line1
line2
line3\
""")
print("######################")

# または以下のようにすると空白行はできないが、読みにくいので、あまりしない。
print("######################")
print("""line1
line2
line3
line4""")
print("######################")

# 文字列の演算もできる。
print('Hi.' * 3 + 'Mike'.)
print('Py' + 'thon')
print('Py''thon')

# 以下のような書き方はエラーとなる
str = 'Py'
print(str 'thon')

# 変数に代入した文字列が含まれるときは+を使用する。
print(str + 'thon')

# 文字列がかなり長いときは、いかのような書き方もできる。
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' \
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)
```

## 12. 文字列のインデックスとスライス

文字列にはインデックスがある。

```python
word = 'python'
print(word[0])
print(word[1])

# 一番最後の文字のインデックスは[-1]
print(word[-1])

# スライスというものが存在する
# インデックス0から2の1つ手前までを表示する場合
print(word[0:2])

# 0は省略できる。一番最初から2の1つ手前までを表示する。
print(word[:2])

# 同様にある点から最後までという省略もできる。
print(word[2:])

# インデックス2から5の1つ手前までを表示する場合
# つまり、「yth」が表示される。
print(word[2:5])

# 最初も最後も省略するとすべて表示される。
print(word[:])

# 文字列を書き換えることもできる
# 以下のような記述はできない。
word[0] = 'j'

word = 'j' + word[1:]

# len()というものがある。
n = len(word)
print(n)
```

## 13. 文字のメソッド

```python
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))
```

## 14. 文字列の代入
```python
>>> 'a is {}'.format('a')
'a is a'
>>> 'a is {}'.format('test')
'a is test'
>>> 'a is {} {} {}'.format(1, 2, 3)
'a is 1 2 3'
>>> 'a is {0} {1} {2}'.format(1, 2, 3)
'a is 1 2 3'
>>> 'a is {2} {1} {0}'.format(1, 2, 3)
'a is 3 2 1'
>>> 'My name is {0} {1}'.format('Daichi', 'Motoi')
'My name is Daichi Motoi'
>>> 'My name is {0} {1}. Watashi ha {1} {0}'.format('Daichi', 'Motoi')
'My name is Daichi Motoi. Watashi ha Motoi Daichi'
>>> 'My name is {name} {family}. Watashi ha {family} {name}'.format(name='Daichi', family='Motoi')
'My name is Daichi Motoi. Watashi ha Motoi Daichi'
>>> '1'
'1'
>>> 1
1
>>> srt(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'srt' is not defined
>>> str(1)
'1'
>>> x = str(1)
>>> type(x)
<class 'str'>
>>> True
True
>>> type(True)
<class 'bool'>
>>>
```

## 15. f-strings

```python
>>> a = 'a'
>>> print(f'a is {a}')
a is a
>>> a = 'b'
>>> print(f'a is {a}')
a is b
>>>
>>> x, y, z = 1, 2, 3
>>> print(f'a is {x}, {y}, {z}')
a is 1, 2, 3
>>> print(f'a is {z}, {y}, {x}')
a is 3, 2, 1
>>>
>>> name = 'Daichi'
>>> family = 'Motoi'
>>> print(f'My name is {name} {family}. Watashi ha {family} {name}')
My name is Daichi Motoi. Watashi ha Motoi Daichi
>>>
```