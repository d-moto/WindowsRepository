year_str = input('Enter your birth of year : ')
year = int(year_str)
number_of_eto = (year + 8) % 12
print(number_of_eto)