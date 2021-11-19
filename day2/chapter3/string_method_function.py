name = 'Benedict'
print(len(name))

name = ' Benedict '
print(len(name))

name = 'Benedict'
comot_space = name.strip()
print(len(comot_space))

print('CAPITAL LETTERS')
print(comot_space.upper())
print(comot_space.lower())
print(comot_space.capitalize())

# fname = input('Enter Firstname: ')
# lname = input('Enter Lastname: ')
# full_name = fname + ' '+ lname
# print(full_name)

print('CLASS EXERCISE')
president1 = input('Enter President1: ')
country = input('Enter Country: ')
year1 = input('Enter Year1: ')
president2 = input('Enter President2: ')
year2 = input('Enter Year2: ')
full_statement = president1 + ' '+ 'was the president in ' + country + ' in the year ' + str(year1)+ ' and handed over to '+ president2+ ' in '+ year2
print(full_statement)


