# 9. printでの出力

print('# 9. printでの出力')
print("""
sep : 引数と引数の間の文字を設定する。（デフォルトではスペース）
end : プリントの末尾の設定をする。（デフォルトでは改行[\\n]）
"""
)
print("""
---
print('1', 'Hi')
print('2', 'Hi', 'Mike')
print('3', 'Hi', 'Mike', sep=',')
print('4', 'Hi', 'Mike', sep=',', end='.\\n')
---
""")

print('1', 'Hi')
print('2', 'Hi', 'Mike')
print('3', 'Hi', 'Mike', sep=',')
print('4', 'Hi', 'Mike', sep=',', end='.\n')