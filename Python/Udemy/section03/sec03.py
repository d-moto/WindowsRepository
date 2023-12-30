# int,str,boolの変数を定義する
x = 1
y = 'String'
z = True

print(f'x = {x}, y = {y}, z = {z}')
print(f'x = {type(x)}, y = {type(y)}, z = {type(z)}')

# 型の上書きと型変換を行う。
x = y  # 上書き
w = '10'

print(f'x = {x}:{type(x)}, y = {y}:{type(y)}')
print(f'w = {w}:{type(w)}')

new_w = int(w)
print(f'new_w = {new_w}:{type(new_w)}')



