import art
print(art.logo)

add_new_bidder = True
auction_bids = {}
while add_new_bidder:
    # TODO-1: Ask the user for input
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    # TODO-2: Save data into dictionary {name: price}
    auction_bids[name] = price

    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if more_bidders == "no":
        add_new_bidder = False
    else:
        print("\n" * 20)

# TODO-4: Compare bids in dictionary
# option 1: find highest bid using a for loop
# highest_bid = 0
# highest_bidder_name = ""
# for bidder in auction_bids:
#     if auction_bids[bidder] > highest_bid:
#         highest_bid = auction_bids[bidder]
#         highest_bidder_name = bidder

# option 2: using the max() function
highest_bidder_name = max(auction_bids, key = auction_bids.get)
highest_bid = auction_bids[highest_bidder_name]

print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}!")
