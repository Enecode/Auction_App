biding = {}

condition = False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
            print(f"The winner is {winner} with a bid of ${highest_bid}")


while not condition:
    name = input("Enter your name: ")
    bid_price = int(input("Enter your biding price: "))
    biding[name] = bid_price

    should_continue = input("are there other bidders who wants to bid? (yes/no): ")

    if should_continue == "no".lower():
        condition = True
        highest_bidder(biding)
