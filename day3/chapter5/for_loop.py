for n in range(10):
    print(n)

print('SYLVIA....................................')

for sylvia in range(10):
    print(sylvia)

states = ['Imo', 'Abia', 'Enugu', 'Anambra', 'Ebonyi']

for x in states:
    print(x)

total = 0
for x in range(31):
    total += x
print(total)

print('EVEN NUMBERS')
even = 2
for x in range(21):
    even += x
print(even)

states = {
    'Imo': 'Owerri',
    'Abia': 'Umuahia',
    'Adamawa': 'Yola',
    'Lagos': 'Ikeja',
    'Oyo': 'Ibadan'
}

for state in states:
    print(states[state])

# to print both key and value
for state, capital in states.items():
    print(f'{state}: {capital}')

# to print only values
for capital in states.values():
    print(capital)


states = {
    'South East':{'Imo': 'Owerri', 'Abia' :'Umuahia','Ebonyi': 'Abakaliki', 'Enugu': 'Enugu' },
    'South West':{'Lagos': 'Ikeja', 'Oyo' :'Ibadan','Ogun': 'Abeokuta', 'Ondo': 'Akure' },
    'South South':{'Akwa Ibom': 'Uyo', 'Delta' :'Asaba','Rivers': 'Port harcourt', 'Bayelsa': 'Yenegoa' },
}
for zones in states:
    print(zones)
    for state, capital in states[zones].items():
        print(f'{state}=> {capital}')
        
    