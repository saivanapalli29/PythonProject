class BankAccoun:
    def __init__(self,balance):
        self.__balance=balance
    def getter(self):
        return self.__balance
    def setter(self,amount):
        if amount<0:
           print("its invalide balance")
        else:
              self.__balance=amount
amount=BankAccoun(1000)
balance=amount.getter()
print(balance)
            