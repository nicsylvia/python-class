def say_hello():
    print('Hello World')

say_hello()

def greetings(name):
    print(f'Hello Mr.{name}!')

greetings('Benedict')
greetings('Alabi')
greetings('Joshua')

def add(num1, num2):
    add = num1 + num2
    print(add)

add(350, 200)
add(150, 400)

# Write a python function that will print out the code below
# Obasanjo was the president in nigeria in the year 1999 and handed over to yaradua in the year 2007
# where obasanjo, Nigeria, 1999, Yaradua and 2007 are parameters of the functions.

def name(name1, country, year1, name2, year2):
    print(f'{name1} was the president in {country} in the year {year1} and handed over to {name2} in {year2}')

name('Obasanjo', 'Nigeria', 1999, 'Yaradua', 2007)

# Create a python function that will print out area of a rectangle
# given the formula area= 1/2 base height, where base = 150 and height = 100

def area_triangle(base, height):
    area = 0.5 * base * height
    print(area)

area_triangle(150, 100)

# Create a pynthon function that will print out perimeter of a rectangle
# given the formular perimeter = 2(l+b), where l = 200 and b = 100

def perimeter_rectangle(length, breadth):
    perimeter = 2 * (length + breadth)
    print(perimeter)

perimeter_rectangle(200, 100)

def get_even_numbers(number):
    x = 1
    while x <= number:
        if x % 2 == 0:
            if x < number:
                print(f'{x},')
            else:
                print(x)
        x += 1

get_even_numbers(20)
