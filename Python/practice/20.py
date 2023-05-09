names = ['Taro', 'Taro2', 'Taro3']
print(names)

scores = [80, 97, 100, 69, 99]
print(sum(scores))

todo = ['note', 'pen', 'apple']
print(len(todo))

colors = ['black', 'blue', 'red', 'white', 'green']
print(colors)
colors.sort()
print(colors)

import random
fruits = ['apple', 'lemon', 'banana', 'orange', 'grape', 'apple2', 'melon', 'watermelon', 'melon2']
random_fruits = random.choice(fruits)
print(random_fruits)

## No.21
print('')
print(' ## No.21 ##')
print('')

numbers = (1, 2, 3, 4, 5)
fruits = ('apple', 'banana', 'orange')
coordinates = (10, 20)
print(numbers[2])
print(len(fruits))

## No.22
print('')
print(' ## No.22 ##')
print('')

person = ('John', 25, 'USA')
name, age, country = person
print(name)
print(age)
print(country)

point = (3, 5)
x, y = point
print(x)
print(y)

date = (2023, 5, 15)
year, month, day = date
print(year)
print(month)
print(day)

measurement = (5.2, 3.8, 7.1)
length, width, height = measurement
print(length)
print(width)
print(height)

data = ('John', 25, 'USA', 'john@example.com')
name, age, country, email = data
print(name)
print(age)
print(country)
print(email)

## No.23
print('')
print(' ## No.23 ##')
print('')

menu = ('pizza', 'pasta', 'salad')
for i in menu:
    print(i)

colors = ('red', 'green', 'blue')
print(len(colors))

coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)

person1 = ('John', 20, 'USA')
person2 = ('Mary', 19, 'Japan')
if person1[0] == person2[0]:
    print('same name')
else:
    print('different name')

dimensions = (10, 20, 30)
w, h, d = dimensions
print(w * h)
