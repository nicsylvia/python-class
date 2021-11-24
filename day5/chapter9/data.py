f = open('data.txt', 'r')
# print(f.read(7))
# print(f.readline())
# print(f.readlines())
for data in f.readlines():
    print(data, end='')
# to print it without spaces, add end='' to it.
f.close()
print(' ')
# another way of writing it without closing 

with open('data.txt', 'r') as f:
    for i in f:
        print(i, end='')