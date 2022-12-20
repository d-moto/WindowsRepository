print('# リストの定義')
r = [1, 2, 3, 4, 5, 1, 2, 3]

print(r)

print('# 要素3がどのindexか調べる。初めにヒットしたものしか出力しない。')
print(r.index(3))

print('# 要素3のサーチを4番目のindexから始める場合。')
print(r.index(3, 4))

print('# 要素の数を数える場合。')
print(r.count(3))

print('# rに5が入っているかどうか。')
if 5 in r:
    print('exist')

print('# リストのソート')
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