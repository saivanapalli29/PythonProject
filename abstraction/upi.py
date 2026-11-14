from payment import Payment

class Upi(Payment):
    def pay(self,amount):
        self.amount = amount
        print(f"amount: {self.amount} deposited to yor account")