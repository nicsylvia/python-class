person = {
    'Name': 'Benedict',
    'Age': 42,
    'Status': 'Married',
    'Complexion': 'Fair',
}
print(person['Age'])
print(person.get('Age'))

person['status'] = True
if person['status'] == True:
    print(f"{person['Name']} is married and his age is {person['Age']}")
