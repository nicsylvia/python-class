import datetime

num1 = 5
num2 = 0

# print(num1/num2)

# with open('data.txt', 'r') as f:
    # f.readlines()

# try:
#     num1 = 5
#     num2 = 0
#     print(num1/num2)
# except:
#     print('There is a Zero division error')

# another way of doing it is:

# try:
#     num1 = 5
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError as e:
#     print(f'There is an error {e}')

try:
    num1 = 5
    num2 = 0
    print(num1/num2)
except ZeroDivisionError as e:
    date = datetime.datetime.now()
    with open('error.txt', 'a') as f:
        f.write(f'\n {date} There is an error {e}')
    
