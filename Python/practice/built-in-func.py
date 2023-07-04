a = 1
b = -1

print(a)
print(b)
print(abs(a))
print(abs(b))

mylist = [True, True, True]
x = all(mylist)
print(x)

mylist = (True, False, 0)
x = all(mylist)
print(x)


mylist = [False, True, False]
x = any(mylist)

mytuple = (0, 1, False)
y = any(mytuple)

myset = {0, 1, 0}
z = any(myset)

print(x, y, z)

mylist = []
x = any(mylist)
print(x)

cat_name = 'tama'
print(f"my cat name is {cat_name}")