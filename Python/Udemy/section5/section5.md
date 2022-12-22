## if文
```python
x = -10
if x < 0:
    print('negative')

else:
    print('positive')

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')
```

## デバッカーを使用して確認してみる

## 比較演算子と論理演算子
```python
# var
a = 1
b = 10
c = -10

# aとbが等しい。
if a == b:
    print('a == b')

# aがbと異なる
if a != b:
    print('a != b')

# aがbよりも小さい
if a < b:
    print('a < b')

# aがbよりも大きい
if a > b:
    print('a > b')

# aがb以下である
if a <= b:
    print('a <= b')

# aがb以上である
if a >= b:
    print('a >= b')

# 共通部分
if a > 0 and b > 0:
    print('a > 0 and b > 0')

# 和集合
if a > 0 or b > 0:
    print('a > 0 or b > 0')
else:
    print('a < 0 or b < 0')
```

## In と Notの使いどころ
```python
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# あまり使わない
if not a == b:
    print('Not equal')
# こちらの方を使う
if a != b:
    print('Not equal')


is_ok = True

# ブーリアン型の場合、ifの後にその変数を書くだけでよい。( if is_ok == True: という書き方をしなくて良い。)
if is_ok:
    print('hello')

if not is_ok:
    print('not hello')
```


## 値が入っていない判定をするテクニック
```python
# Falseと判定されるもの
# 0, 0.0, '', [], (), {}, set()

is_ok = True
is_ok = 1
is_ok = ''
is_ok = 'abc'
is_ok = []
is_ok = [1]


if is_ok:
    print('OK')
else:
    print('NO')
```

## Noneを判定する場合
```python
is_empty = None
print(is_empty)
print(help(is_empty))

# あまり使わない。
if is_empty == None:
    print('None!!')

# 以下を使う。
if is_empty is None:
    print('None!!')

if is_empty is not None:
    print('Not None!!')

print(1 == True)
print(1 is True)
print(True is True)
print(None is None)
```

## while文とcontunue文とbreak文

## while else文

## while else文

## input関数

## for文とbreak文とcontinue文

## for else文

## range関数

## enumerate関数

## zip関数

## 辞書をfor文で処理する

## 関数定義

## 関数の引数と返り値の宣言

## 位置引数とキーワード引数とデフォルト引数

## デフォルト引数で気を付けること

## 位置引数のタプル化

## キーワード引数の辞書化

## Docstringsとは

## 関数内関数

## クロージャー

## デコレーター

## ラムダ

## ジェネレーター

## リスト内包表記

## 辞書包括表記

## 集合包括表記

## ジェネレーター内包表記

## 名前空間とスコープ

## 例外処理

## 独自例外の作成