print("Welcome to the secret auction program!!!")

bids = {}

while True:
    name = input("Whats your name?\n")
    bid = input("Whats your bid?\n")

    bids[name] = bid
    
    loop = input("Are there any other biders (Y/N)?\n")

    print("\n" * 100)

    if loop == 'Y' or loop == 'y':
        continue
    elif loop == 'N'or loop == 'n':
        break

highest_bid = 0
highest_bidder = ''

for bider in bids:
    if int(bids[bider]) > highest_bid:
        highest_bid = int(bids[bider])
        highest_bidder = bider

print(f"{highest_bidder} won with the bid of {highest_bid}")