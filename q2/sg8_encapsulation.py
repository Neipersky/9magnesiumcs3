class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The amount should not be a negative number.")
