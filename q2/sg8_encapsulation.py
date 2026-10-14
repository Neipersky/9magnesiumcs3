class BankAccount:
    def __init__(self, account_number: int, initial_balance: float = 0.0):
        self.__account_number = account_number
        self.__balance = initial_balance if initial_balance >= 0 else 0.0
    def set_account_number(self, account_number: int):
        self.__account_number = account_number
    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must be not be a negative number.")
    @property
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance
if __name__ == "__main__":
    account_1 = BankAccount(12345, 1000)
    print("Account 1")
    print("Account Number:", account_1.account_number)
    print("Balance: {:.2f}".format(account_1.balance))
    print()
    print("Update balance to -100")
    account_1.set_balance(-100)
    print("Account Number:", account_1.account_number)
    print("Balance: {:.2f}".format(account_1.balance))
