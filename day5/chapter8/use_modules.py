# Here's the file that we will use to import from the code_module.
import code_module

class Developer(code_module.Employee):
    def detail(self):
        statement = 'Employee detail below \n'
        statement += f'Firstname: {self.f} \n'
        statement += f'Lastname: {self.l} \n'
        statement += f'salary: {self.salary()} \n'
        return statement

d1 = Developer('Benedict', 'Uwazie', 1500)
print(d1.salary())

code_module.get_even_numbers(13)