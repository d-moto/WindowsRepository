# Pythonの基本

## 8. 変数宣言

- **変数宣言**

  pythonでは、int,srtなど変数の宣言時に指定する必要はない。  
  変数のタイプは`type()`関数で確認できる。

  ```python
  num = 1
  name = 'Mike'
  is_ok = True 
  print(num, type(num))
  print(name, type(name))
  print(is_ok, type(is_ok))
  ```
  ```text
  1 <class 'int'>
  Mike <class 'str'>
  True <class 'bool'>
  ```

- **型の上書きと型変換**
  
  以下のようにすると、変数の上書きと、型変換ができる
  - 型の上書き
    ```
    # 型の上書き
    num = 1
    name = 'Mike'
    
    num = name
    
    print(num, type(num))
    ```
    ```text
    Mike <class 'str'>
    ```
    
  - 型の変換
    ```python
    # 型の変換
    name = '1'
    
    new_num = int(name)
    
    print(new_num, type(new_num))
    ```
    ```text
    1 <class 'int'>
    ```
    
- **型の宣言**
  
  一応Python3.9から型の宣言ができる
  ```text
  <var name>: <type> = <value>
  ```
  ```python
  num: int = 1
  name: str = 'Mike'
  ```
  ただ基本的に使用しない。

- **変数の命名**  
  Pythonでは、変数の先頭に数字は使用できない。  
  また、予約語も変数の名前には使用できない。

## 9. printで出力

- sep : 引数と引数の間の文字を設定する。（デフォルトではスペース）
- end : プリントの末尾の設定をする。（デフォルトでは改行[\n]）
```python
print('1', 'Hi')
print('2', 'Hi', 'Mike')
print('3', 'Hi', 'Mike', sep=',')
print('4', 'Hi', 'Mike', sep=',', end='.\n')
```
```text
1 Hi
2 Hi Mike
3,Hi,Mike
4,Hi,Mike.
```

## 10. 数値

### 数値の扱い

- 四則演算
```python
print(2 + 2)
print(5 - 2)
print(5 * 6)
print(50 - 5 * 6)
print((50 - 5) * 6)
print(8 / 5)
print(0.6)
print(.6)
print(17 / 3)
print(17 // 3)
print(17 % 3)
print(5 ** 5)
pie = 3.14159265358979
print(pie)
print(round(pie, 2))
```
```
4
3
30
20
270
1.6
0.6
0.6
5.666666666666667
5
2
3125
3.14159265358979
3.14
```

```shell
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
```

### 数学関数
```python
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)
```

### ドキュメントの表示
```python
import math
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
print('Hi.' * 3 + 'Mike')
print('Py' + 'thon')
print('Py''thon')

# 以下のような書き方はエラーとなる
# stri = 'Py'
# print(stri 'thon')
## いいえ、print(str 'thon')は構文エラーを引き起こしますが、それはPythonインタプリタによってキャッチされます。

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

```
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
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
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
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
 |  __getnewargs__(...)
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
 |  __mod__(self, value, /)
 |      Return self%value.
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
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |      
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |  
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |      
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  ★rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  ★startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(...)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

None

Process finished with exit code 0
```

```python
s = 'My name is Mike. Hi Mike.'
print(s)

# startswithメソッド。引数の値から文字列が始まっていれば、Trueが返される。
is_start = s.startswith('My')
print(is_start)

# Falseが返される。
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

num = 0
for i in s:
    print("{} : {}".format(num, i))
    num += 1

```

## 14. 文字列の代入
```shell
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

```shell
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