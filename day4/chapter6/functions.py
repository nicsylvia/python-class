def office(name, color='Yellow'):
    print(f'The color of {name} is {color}.')

office('MTN')
office('Alabian', 'Skyblue')

def get_even_numbers(number, start=1):
    while start <= number:
        if start % 2== 0:
            if start < number:
                print(f'{start},')
            else:
                    print(start)
        start += 1

print('EVEN NUMBERS FROM 1 TO 10')
get_even_numbers(10)
print('EVEN NUMBERS FROM 10 TO 50')
get_even_numbers(50, 10)
        