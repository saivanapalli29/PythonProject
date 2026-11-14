from upi import Upi as UPI
amount=int(input("enter amount:"))
payment=UPI()
payment.pay(amount)