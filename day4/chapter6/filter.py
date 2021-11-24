def even_numbers(x):
    if x % 2 == 0:
        return x

get_even = list(filter(even_numbers, [2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(get_even)

# another example using map. 
# iterable....iteratable. takes a funtion and an iterable
# map is another built-in function.

def double_number(x):
    x *= 2
    return x

get_double = list(map(double_number, range(1, 11)))
print(get_double)
