## No.24
print('')
print(' ## No.24 ##')
print('')

person = {
    'name': 'John',
    'age': 27,
    'country': 'USA'
}

fruits = {}

book = {
    'title': 'muder x',
    'author': 'higashino',
    'year': '2002'
}

print(person['name'])

print(len(book))


## No.25
print('')
print(' ## No.25 ##')
print('')

print(list(person.keys()))

print(list(fruits.values()))

book['genre'] = 'Mystery'

del person['age']

fruits['name'] = 'apple'
fruits['num'] = '10'

for key, value in fruits.items():
    print(key, value)

print(fruits.items())