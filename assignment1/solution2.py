number_one = input('Enter First number: ')
number_two = input('Enter Second number: ')
number_three = input('Enter Third number: ')

if number_one > number_two < number_three:
    print(f'The number {number_two} is the lowest number here')

elif number_two > number_one < number_three:
    print(f'The number {number_one} is the lowest number here')

elif number_one > number_three < number_two:
    print(f'The number {number_three} is the lowest number here')

else:
    print('An error occured somewhere. Recheck your codes!')

print('*******************************************')
print('Nested If Approach')
print('        ')

a = input('Enter First number: ')
b = input('Enter Second number: ')
c = input('Enter Third number: ')

if b > a:
    if c > a:
        print(f'The number {a} is the lowest number supplied')

if a > b:
    if c > b:
        print(f'The number{b} is the lowest number supplied')

if a > c:
    if b > c:
        print(f'The number {c} is the lowest number supplied')

else:
    print('An error occured. Please recheck!!') 