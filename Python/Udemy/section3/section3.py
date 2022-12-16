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