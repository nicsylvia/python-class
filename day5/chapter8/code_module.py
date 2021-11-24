# A module is a file where you can store all your python code and use them by importing them.
class Employee():
    pay_raise= 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        return self.p * self.pay_raise + self.p

#  docstring: it comes up as an explanation when this module page is imported
def get_even_numbers(number):

    '''
    This function takes one parameter and returns integer
    of even numbers.
    '''
    x = 1
    while x <= number:
        if x % 2 == 0:
            if x < number:
                print(f'{x},')
            else:
                print(x)
        x += 1
