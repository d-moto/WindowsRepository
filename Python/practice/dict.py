## No.24
print('')
print(' ## No.24 ##')
print('')

print('1. ')
person = {
    'name': 'John',
    'age': 27,
    'country': 'USA'
}
print('')

print('2. ')
fruits = {}
print('')


print('3. ')
book = {
    'title': 'muder x',
    'author': 'higashino',
    'year': '2002'
}
print('')

print('4. ')
print(person['name'])
print('')

print('5. ')
print(len(book))
print('')

## No.25
print('')
print(' ## No.25 ##')
print('')

print('1. ')
print(list(person.keys()))
print('')

print('2. ')
print(list(fruits.values()))
print('')

print('3. ')
book['genre'] = 'Mystery'
print('')

print('4. ')
del person['age']
print('')

print('5. ')
fruits['name'] = 'apple'
fruits['num'] = '10'

for key, value in fruits.items():
    print(key, value)

print(fruits.items())
print('')


## No.26
print('')
print(' ## No.26 ##')
print('')

print('1. ')
person_copy = person.copy()
print(person_copy)
print('')

print('2. ')
book_copy = book.copy()
print(book_copy)
print('')

print('3. ')
fruits_copy = dict(fruits)
print(fruits_copy)
print('')

print('4. ')
print(person)
print(person_copy)
print('')

print('5. ')
print(book)
print(book_copy)
print('')


## No.27
print('')
print(' ## No.27 ##')
print('')

print('1. ')
student = {
    'name': 'Alice',
    'age': 17,
    'grade': 10
}
print(student)
print('')

print('2. ')
car = {
    'make': 'Japan',
    'model': 'Camry',
    'year': 2023
}
print(car)
print('')

print('3. ')
product = {
    'name': 'iPhone',
    'price': 140000,
    'quantity': 10
}
print(product)
print('')

print('4. ')
country = {
    'name': 'Japan',
    'population': 240000000,
    'capital': 'Tokyo'
}
print(country)
print('')

print('5. ')
person['email'] = 'john@example.com'
print(person)
print('')