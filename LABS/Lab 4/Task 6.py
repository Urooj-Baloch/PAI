class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__date_of_opening = date_of_opening
        self.__balance = balance
    # Getter and Setter methods
    def get_account_number(self):
        return self.__account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number
    def get_customer_name(self):
        return self.__customer_name
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name
    def get_date_of_opening(self):
        return self.__date_of_opening
    def set_date_of_opening(self, date_of_opening):
        self.__date_of_opening = date_of_opening
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount,"New Balance: ",self.__balance)
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount,"Remaining Balance:" ,self.__balance)
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    def check_balance(self):
        print("Current Balance:", self.__balance)
        return self.__balance
account = BankAccount("12345", "Urooj Baloch", "2023-01-15", 5000)
print("Account Number: ",account.get_account_number())
print("Customer Name:", account.get_customer_name())
print(f"Date of Opening:", account.get_date_of_opening())
account.deposit(10000)
account.withdraw(5000)
account.check_balance()
