fname = 'Daniel'
lname = 'Umeh'
with open('data.txt', 'a') as f:
    f.write(f'\n {fname} {lname}')