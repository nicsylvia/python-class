# 4. Write a program that sums all the numbers in a list 10, 20, 30, 40, 70, 200, 300 and also determine 
# the average.
# used for-loop to achieve this.
# Average is sum/length of the list.


list_numbers= [10, 20, 30, 40, 70, 200, 300]

sum = 0
for numbers in list_numbers:
    sum += numbers
print(f'The sum is {sum}')

print('     ')

print(f'The Average is {sum/len(list_numbers)}')


