class Account:
    def __init__(self):
        self.__account_no = "0"
        self.__account_bal = 0.0
        self.__security_code = ""

    def initialize(self, number, balance, code):
        self.__account_no = number
        self.__account_bal = balance
        self.__security_code = code

    def print_details(self):
        print("Account Details:")
        print(f"Account Number: {self.__account_no}")
        print(f"Account Balance: ${self.__account_bal}")
        print(f"Security Code: {self.__security_code}")
acc1 = Account()
acc1.initialize("232005", 8900.99, "Fast1234")
acc1.print_details()
