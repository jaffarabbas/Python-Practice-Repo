# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber 
# (numeric type), name (name of the account owner as string type), balance. Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions. Create a Withdrawal() method  which manages withdrawals actions. Create an bankFees() method to apply
# the bank fees with a percentage of 5% of the balance account. Create a display() method to display account details. Give the complete code for the  BankAccount class.
# the  BankAccount class.Output:The output is :

# Account Number :   0000-0000-123

# Account Name :  Your Name

# Account Balance :  Rs. 5000

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount

    def Withdrawal(self, amount):
        self.balance -= amount

    def bankFees(self):
        self.balance *= 0.95

    def display(self):
        print("Account Number: ", self.accountNumber)
        print("Name: ", self.name)
        print("Balance: ", self.balance)

account = BankAccount("0000-0000-123", "Your Name", 5000)
account.Deposit(1000)
account.Withdrawal(500)
account.bankFees()
account.display()


