### 変数宣言
print("#######################")
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

print("#######################")
num = name
print(num, type(num))

print("#######################")
name = '1'
new_num = int(name)
print(new_num, type(new_num))

print("#######################")
print('1', 'Hi')
print('2', 'Hi', 'Mike')
print('3', 'Hi', 'Mike', sep='!!')
print('4', 'Hi', 'Mike', sep='!!', end='???\n')

print("#######################")
print('01 : ', 2 + 2)
print('02 : ', 5 - 2)
print('03 : ', 5 * 2)
print('04 : ', 50 - 5 * 2)
print('05 : ', (50 - 5) * 2)
## ↓folat型となる
print('06 : ', 8 / 5)
print('07 : ', 0.6)
print('08 : ', .6)
## ↓丸め誤差
print('09 : ', 17 / 3)
## 商
print('10 : ', 17 // 3)
## 余り
print('11 : ', 17 % 3)
print('12 : ', 5 ** 5)
pie = 3.14159265358979
print('13 : ', pie)
## 小数点2桁まで
print('14 : ', round(pie, 2))

print("#######################")
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

print("#######################")
##print(help(math))