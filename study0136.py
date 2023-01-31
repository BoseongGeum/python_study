import random

class Account:

    account_count = 0
    
    def __init__(self, name, bal):
        self.bank_name = "SC은행"
        self.name = name
        self.bal = bal

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.num = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def info(self):
        print("은행이름:", self.bank_name)
        print("예금주:", self.name)
        print("계좌번호:", self.num)
        print("잔고:", f"{self.bal:,}원")


    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, money):
        if money > 0:
            self.bal += money

    def withdraw(self, money):
        if money < self.bal:
            self.bal -= money

geum = Account("금보성", 10000)
geum.info()
