# A constructor is as special method that will run when  you create an instance of a class that is an object.


class car():
    doors = 4
    wheels = 4

    def __init__(self):
        print('This is constructor')


    def detail(self, name):
        return f'The name of this car is {name} it has {self.wheels} wheels and {self.doors} Doors '

c1 = car()
print(c1.detail('BMW'))

