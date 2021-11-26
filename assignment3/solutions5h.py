from solutions5 import MyBankAccount

class SubMyBankAccount(MyBankAccount):
    def __init__(self, first_name, last_name, principal, time, rate):
        super().__init__(first_name, last_name)
        self.principal = principal
        self.time = time
        self.rate = rate

    def interest(self):
        interest = (self.principal *  (self.time/12) * self.rate)/100
        return interest

b1 = SubMyBankAccount('Daniel', 'David', 45000, 6, 0.1)
print(b1.interest())