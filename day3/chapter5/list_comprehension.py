numbers = []

for n in range(1, 11):
    numbers.append(n)
print(numbers)

even_numbers = []
for n in range(1, 21):
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)

print('LIST COMPREHENSION')

even_numbers = [n for n in range(1, 21) if n % 2 == 0]
print(even_numbers)

numbers = [n for n in range(1, 11)]
print(numbers)