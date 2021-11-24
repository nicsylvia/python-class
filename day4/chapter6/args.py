def addition(*args):
    total = 0
    for a in args:
        total += a
    print(total)

addition(10, 5, 3)

# another example
def multiplication(*args):
    total = 1
    for a in args:
        total *= a
    print(total)

multiplication(3, 2, 2)

# another example
def show_states(*args):
    for state in args:
        print(state)

show_states('Imo', 'Abia')
show_states('Imo', 'Abia', 'Abuja', 'Lagos')
