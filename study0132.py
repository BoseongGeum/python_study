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
        print(self.bank_name, self.name, self.num, self.bal)

Geum = Account("금보성", 150)
print(Account.account_count)
kim = Account("김민수", 100)
print(Account.account_count)
lee = Account("이민수", 100)
print(Account.account_count)
