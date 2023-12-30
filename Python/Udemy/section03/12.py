import sys
import time

word = 'Python'
print(word)
print(word[0])
print(word[2])
print(word[0], word[1], word[2], word[3])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])
# 存在しないindexはエラーとなる。
# print(word[-7])

# 0,1が出力される。index:0 - index:2の手前まで。
print(word[0:2])
print(word[1:4])

print(word[:5])

print(word[3:])
print(word[:])

word = 'J' + word[1:]
print(word)

print(len(word))

s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('XX')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
# print(help(str))

i = 0
for i in range(len(s)):
    print(f"index:{i} = {s[i]}")


print(sys.executable)
# print(help(sys))
print(sys.copyright)
print(sys.version)
print(sys.path)

dic = {1: 1, 2: 2, 'yes': True}
print(dic)
print(dic[1])
print(dic['yes'])
time.sleep(100)
input("Enter....")
