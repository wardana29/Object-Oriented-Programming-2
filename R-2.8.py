class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self.acnt = acnt
        self.customer = customer
        self.bank = bank
        self.limit = limit
        self.balance = balance
    def __repr__(self):
        return 'CreditCard->{} {} {} {} {}'.format(self.customer, self.bank, self.acnt, self.limit, self.balance)
  
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
    wallet = []
    wallet.append(CreditCard( "Mihra" , "Konawe" , "012345" , 4000) )
    wallet.append(CreditCard( "Mihra" , "Konawe Selatan" , "123450" , 5000) )
    wallet.append(CreditCard( "Mihra" , "Kendari" , "543210" , 6000) )
    for val in range(1, 10):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
    print('wallet 1:{} wallet 2:{} wallet 3:{}'.format(wallet[0].balance, wallet[1].balance,wallet[2].balance))
    for c in range(3):
        print( "Customer = ", wallet[c].get_customer())
        print( "Bank =" , wallet[c].get_bank())
        print( "Account = ", wallet[c].get_account())
        print(" Limit =" , wallet[c].get_limit())
        print( "Balance =" , wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print( "New balance =" , wallet[c].get_balance())
        print()