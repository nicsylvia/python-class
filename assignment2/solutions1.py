# 1. Create a multiplication table program using while loop, this will be done in such a way that when a 
# user supplies any number the multiplication table of that number will be created.
# created an input first then used while loop to achieve it.

Number = int(input('Enter the Multiplication table you want: '))
print('    ')

print(f'Multiplication Table of {Number}: ')

n = 1

while n <= 12:
    print(f'{Number} x {n}= {Number} * {n}')
    n += 1

print('THANK YOU FOR CODING WITH US.')
print('REACH OUT TO US FOR YOUR MULTIPLICATION TABLE OUTPUT')

# Questions:
# in the print area, why do we have to put a comma at the end of all of them.
#  I noticed the other ways we concatenate strings didn't work for it.