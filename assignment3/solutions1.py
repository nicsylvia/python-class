#1. Create a multiplication table function using while loop, this function should take three argument 
# the multiplication table number, the start value, the stop value. The start value and stop value 
# should take default values of your choice. It will be done in such a way that when you pass one 
# number the multiplication table of that number will be generated along with the default start and 
# stop values. These default start and stop values can also be overwritten when you pass them as an 
# argument when calling the function.

# Created 3 functions, then used the while loop, then call the function much later.
# NB: It's better to always put the increment after the print out so that it loops properly.

print('MULTIPLICATION TABLE.')
print('        ')
def multiplication_table(number, start_value, stop_value):
    while start_value <= stop_value:
        print(number, 'x', start_value, '=', number * start_value)
        start_value += 1

multiplication_table(2, 1, 12)
print(   )
multiplication_table(10, 1, 12)



# questions:
# 1. Does for loop uses only a list kind to work.
# 2. Can we use for loop to do multiplication table.