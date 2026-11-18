class Account:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Total balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        if self.balance == 0:
            print("Zero balance")
        else:
            print("Normal")
        print("Balance:", self.balance)

sbi = Account("Kiran", "21112-122", 20000)
sbi.deposit(200)
sbi.withdraw(300)
sbi.display_balance()
