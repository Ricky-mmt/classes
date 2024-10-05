class BankAccount:
    interest_rate = 0.05

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


####Create two instances of BankAccoun
account1 = BankAccount("ricky")
account2 = BankAccount("okello")

##Perform deposits and withdrawals
account1.deposit(30000)
account2.withdraw(40000)
account2.deposit(70000)
##Apply interest
account1.apply_interest()
account2.apply_interest()
## Display account information
account1.display_account_info()
account2.display_account_info()