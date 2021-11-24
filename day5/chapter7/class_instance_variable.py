# class variable is one in which its variable doesn't change across several instances.

class Employee():
    pay_raise= 0.10

    def __init__(self, first_name, last_name, pay):
        self.f = first_name
        self.l = last_name
        self.p = pay

    def salary(self):
        return self.p * self.pay_raise + self.p
    
e1 = Employee('Benedict', 'Uwazie', 12000)
print(e1.p)
print(e1.salary())

e2 = Employee('Adebayo', 'Alabi', 1500)
print(e2.p)
print(e2.salary())