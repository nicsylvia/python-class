# super is used to modify a method defined in a parent class in a child class.# inheritance is an oop concept that helps us to avoid redundacy.
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

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.pro = prog_lang

    def detail(self):
        statement = 'Employee detail below \n'
        statement += f'Firstname: {self.f} \n'
        statement += f'Lastname: {self.l} \n'
        statement += f'Programming Language: {self.pro} \n'
        statement += f'salary: {self.salary()} \n'
        return statement
    

d1 = Developer('Benedict', 'Uwazie', 1200, 'python')
print(d1.salary())
print(d1.pro)



     
    