import os
def find_bidder(bidder_details):
    highest_price=0
    winner=""
    for bidder in bidder_details:
        bidder_price=bidder_details[bidder]
        if bidder_price>highest_price:
            highest_price=bidder_price
            winner=bidder

    print(f"here the bidder details {bidder_details}")
    print(f"the winner is {winner} highest bid price is {highest_price}")

bidder_data={}
end_of_bid=False
while not end_of_bid:
    name=input("Enter your name: ")
    price=int(input("Enter your price: "))
    bidder_data[name]=price
    more_bidders=input("Do you have more bidders? (yes/no): ").lower()
    if more_bidders=="no":
       end_of_bid=True
       find_bidder(bidder_data)
    # elif more_bidders=="yes":

        # os.environ.setdefault("TERM", "xterm")
        # os.system("clear")