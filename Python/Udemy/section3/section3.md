# Pythonの基本

## 1. 変数宣言

</br>

### **変数宣言**
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

### **型の上書きと型変換**
</br>

以下のようにすると、変数の上書きと、型変換ができる

型の上書き
```python
num = 1
name = 'Mike'

num = name

print(num, type(num))
```
↓ 実行結果
```python
Mike <class 'str'>
```

型の変換
```python
name = '1'

new_num = int(name)

print(new_num, type(new_num))
```
↓ 実行結果
```python
1 <class 'int'>
```

### **型の宣言**
</br>

一応Python3.9から型の宣言ができる
```python
num: int = 1
name: str = 'Mike'
```
ただ基本的に使用しない。

### **変数の命名**
Pythonでは、変数の先頭に数字は使用できない。
また、予約語も変数の名前には使用できない。

</br>

## 2. printで出力
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

## 3. 数値
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

## 4. 文字列
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