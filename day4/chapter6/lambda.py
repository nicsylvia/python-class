# lambda is the shorthand way of writing functions.

# to add 2 values
add = lambda x, y: x+y
print(add(5, 3))

# to multiply 3 values
triple = lambda x,y, z: x*y*z
print(triple(3, 4, 5))

# to find the area of a triangle
area = lambda base, height: 0.5 * base * height
print(area(10, 30))

# to check if the number is even
even = lambda x: x if x % 2 == 0 else False
print(even(15))

# to filter and print out even numbers
get_even = list(filter(lambda x : x if x % 2 == 0 else False, range(11)))
print(get_even)

# using map to double by 2
double_number = list(map(lambda x: x*2, range(1, 11)))
print(double_number)