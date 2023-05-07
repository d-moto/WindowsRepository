numbers = [1, 2, 3, 4, 5]
print(numbers.count(5))

fruits = ['apple', 'pineapple', 'orange', 'grape']
print(fruits.sort())

print(sum(numbers))

language = ["Python", "Java", "C++", "JavaScript", "Ruby"]
language.append('Swift')
print(language)

fruits.append('banana')
print(fruits)
fruits.remove('banana')
print(fruits)


numbers_copy = numbers.copy()
language_copy = language[:]
fruits_copy = fruits.copy()
print(numbers)
print(numbers_copy)

print(language)
print(language_copy)


