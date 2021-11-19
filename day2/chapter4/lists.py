students = ['Joan', 'Sylvia', 'Diamond', 'Davidson']
print(students[0])

data = ['Obasanjo', 'Nigeria', 1999, 'Yaradua', 2007]
statement = f'{data[0]} was the president in {data[1]} in the year {data[2]} and handed over to {data[3]} in {data[4]}'
print(statement)

fruits = ['apple', 'banana', 'cherry']

fruits.append('mango')
print(fruits)

fruits.insert(2, 'guava')
print(fruits)

fruits[1] = 'udara'
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

print(len(fruits))


