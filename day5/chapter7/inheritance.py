# inheritance is an oop concept that helps us to avoid redundacy.
class Employee():
    pay_raise= 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        return self.p * self.pay_raise + self.p

 # This is a child class.
#  \n makes it starts on a new line on the terminal.

class Developer(Employee): 

    def detail(self):
        statement = 'Employee detail below \n'
        statement += f'Firstname: {self.f} \n'
        statement += f'Lastname: {self.l} \n'
        statement += f'salary: {self.salary()} \n'
        return statement
    # pass

d1 = Developer('Benedict', 'Uwazie', 1200)
print(d1.salary())
print(d1.detail())

d2 = Developer('Alabi', 'Adebayo', 1400)
print(d2.salary())
print(d2.detail())

     
    