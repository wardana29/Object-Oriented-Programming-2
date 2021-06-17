class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self.acnt = acnt
        self.customer = customer
        self.bank = bank
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        return self.customer
    def get_bank(self):
        return self.bank
    def get_account(self):
        return self.acnt
    def get_limit(self):
        return self.limit
    def get_balance(self):
        return self.balance
    def charge(self, price):
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True
    def make_payment(self, amount):
        if amount < 0:
            raise ValueError('Amount cannot be negative')
        self.balance -= amount
        
if __name__ == '__main__':
    card = CreditCard('Mihra Wardana','BRI','121231332',200)
    card.make_payment(-100)
print(card.__dict__)