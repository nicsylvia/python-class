# 2. Write a program in python that tells if the name you supplied is in a list or the name is not in a list.
# created a list first then an input for names to be entered. Then using if, elif and else i achieved this.
# Then used for loop to output all thenames at the ending.

list_of_names = ['Joan', 'Ramadan', 'Sylvia', 'Davidson', 'Daniel', 'Abdul', 'Alabi', 'Benedict', 'Uche', 'Habeeb','Cynthia']

intro = "Hello People, Welcome to the grand-finale of Alabian Solutions lucky draw. Please enter your name to check if you're among the lucky winners."
print(intro.upper())

print('           ')

names = input('Enter Your Name: ')

if names == list_of_names[0]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[1]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[2]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[3]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[4]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[5]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[6]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[7]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[8]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[9]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
elif names == list_of_names[10]:
    print(f'Hey {names}, Congrats!!! your name is in the list.')
else:
    print(f'Oops!! sorry {names} your name is not in the list. Try again next time. Goodluck')

print('             ')

print('Here are the names on the list.')

input('Press y if you still want to view the name: ')

print('       ')

print('The Lucky Winners are: ')
for names in list_of_names:
    print(names)




# questions i have:
# 1. Can't we use function to do this.
# 2. What if i wanted to do something like press y to proceed and if you don't want press n ....how do i go about it