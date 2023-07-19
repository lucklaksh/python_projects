from replit import clear
from art import logo
print(logo)
print("Welcome to the Secret Auction Program\n")
repeat ='yes'
auction = []
max_bid=0
# name = ""
while(repeat != 'no'):
    dict_bid = {}
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    dict_bid = {
        "name" : name,
        "bid": bid,
    }
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    auction.append(dict_bid)
    if(bidders != 'yes'):
        repeat = bidders
    clear()

for item in auction:
    if item["bid"] > max_bid:
        max_bid= item["bid"]
        name = item["name"]

print(f"The Winner is {name} with a bid of {max_bid}")