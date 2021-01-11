class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def inquire(self):
        print(f"잔액은 {self.balance}원 입니다.")

account = Account(8000)
account.deposit(1000)
account.deposit(1000)
account.inquire()

shinhan = Account(8000)
shinhan.deposit(1000)
shinhan.inquire()

nonghyup = Account(1200000)
nonghyup.inquire()


li1 = [1, 2, 3]
li1.append(12)
