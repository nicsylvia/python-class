number_one = input('Enter First number: ')
number_two = input('Enter Second number: ')
number_three = input('Enter Third number: ')

if number_one < number_two and number_three:
    print(f'The number {number_one} is the lowest number here')

elif number_two > number_one and number_three:
    print(f'The number {number_two} is the lowest number here')

elif number_three < number_one and number_two:
    print(f'The number {number_three} is the lowest number here')

else:
    print('An error occured somewhere. Recheck your codes!')
