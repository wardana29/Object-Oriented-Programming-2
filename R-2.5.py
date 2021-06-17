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
        else:
          self.balance += price
          return True
    def make_payment(self, amount):
        self.balance -= amount
        
if __name__ == '__main__':
   card = CreditCard('Mihra Wardana','BRI','121231332',200)
   card.charge(80)
print(card.__dict__)