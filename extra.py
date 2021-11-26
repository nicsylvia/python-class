class bankaccount():
    def __init__(self, deposit, balance, withdraw):

        # function to deposit alert
        def deposit(self):
            amount = float(input("Enter amount to be deposited: "))
            self.balance += amount
            print("\n Amount Deposited:", amount)

            # funtion to withdraw the amount

            # 5. Create a class called MyBankAccount with three methods
# a. The first method will be an init method, the init method will take two argument, firstname, lastname
# b. Use the firstname, lastname to form the user’s email address in the init method
# c. Lowercase the email address
# d. Set the balance to be equal to zero in the init method
# e. Create a method that will enable a user to deposite money in his account, the amount will supplied from 
# the command promt
# f. Create a method that will show the amount that have been withdrawn, this amount will be supplied 
# from the command prompt and also detect insufficient funds on the account
# g. Create a method that will display the balance
# h. Create a child class and use the from keyword to import the parent class
# i. The init method of this child class should take more additional arguments such as principal, rate, 
# time
# ii. Create a method that will display the user’s detail such as phone, email, firstname, lastname
# iii. Create another method that will calculate the interest when a user borrows a money for a 
# period of time let’s say 1year or 2years using 5% rate using this formular (I = (P*R*T)/100
# i. Lastly test the methods created

# SOLUTION:
class MyBankAccount():
    def __init__(self):
        self.balance = 0
        self.deposit = 0
        self.withdraw = 0
        self.display = 0
        
    # def __init__(self, deposit, withdraw, display):
    #     self.deposit = deposit
    #     self.withdraw = withdraw
    #     self.display = display

        # def __init__(self, first_name, last_name):
        #     self.first_name = User_Email_Address
        #     self.first_name.lower()
        #     self.balance = 0
        def deposit(self):
            amount = float(input("Enter amount to be deposited: "))
            self.balance += amount
            print("\n Amount Deposited:", amount)
        def withdraw(self):
            amount = float(input("Enter amount to be withdrawn: "))
            if self.balance >= amount:
                self.balance -= amount
                print("\n You withdrew:", amount)
            else:
                print("\n Insufficient balance")
        def display(self):
            print("\n Net Available Balance = ", self.balance)
s = MyBankAccount()
s.deposit()
s.withdraw()
s.display()

try:
    print("A slight glitch occured please")
except:
    print("Check back later")
    

   

