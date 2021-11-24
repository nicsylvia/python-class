class car():
    doors = 4
    wheels = 4
# method is a function inside a class. Every method must have the name self as its first parameter.
    def detail(self, name):
        return f'The name of this car is {name} it has {self.wheels} wheels and {self.doors} Doors '

c1 = car()
print(c1.doors)
print(c1.wheels)
print(c1.detail('Mazda'))
c2 = car()
c2.doors = 2
c2.wheels = 2
print(c2.detail('Unicar'))