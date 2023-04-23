# 8. 変数宣言
## 変数宣言
print('## 変数宣言')
print('以下のように宣言した場合の型は以下のようになる。')
print("""
---
num = 1
name = 'MIke'
is_ok = True
---
""")

num = 1
name = 'MIke'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))
print('\n')

## 型の上書き
print('## 型の上書き')
print('以下のようにnumにnameを代入すると、numの方は、nameの型で上書きされる。')
print("""
---
num = 1
name = 'Mike'

num = name
print(num, type(num))
---
"""
)

num = 1
name = 'Mike'
num = name
print(num, type(num))
print('\n')

## 型の変換
print('## 型の変換')
print('int(var)により、str型の"1"はint型へ変換される。')
print("""
---
name = '1'
new_num = int(name)
print(new_num, type(new_num))
---
""")

name = '1'
new_num = int(name)
print(new_num, type(new_num))
print('\n')

## 型の宣言
print('## 型の宣言')
print('python3.9から型の宣言ができるが基本的に使用しない。★ バグの原因となりやすいため')
print("""
---
num: int = 1
name: str = 'Mike'
---
""")

num: int = 1
name: str = 'Mike'
print('\n')

