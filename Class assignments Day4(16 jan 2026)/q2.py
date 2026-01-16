class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        print("Account number=",self.account_number,"Balance=",self.balance)
    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount cannot be zero and should be positive")
        else:
            self.balance=self.balance+amount
            print("Balance is ",self.balance)
    def withdraw(self,amount):
        if amount<0:
            print("Enter the amount greater than zero")
        elif amount<self.balance:
            self.balance=self.balance-amount
            print("Balance is ",self.balance)
        else:
            print("Amount can't be withdrawn as it is greater than balance")
    def __del__(self):
        print("Object has been deleted")
b=BankAccount(1,100)
deposit_amount=int(input("Enter the amount you want to deposit"))
b.deposit(deposit_amount)
withdraw_amount=int(input("Enter the amount you want to withdraw"))
b.withdraw(withdraw_amount)