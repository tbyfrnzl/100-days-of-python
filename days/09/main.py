import art

print(art.logo)

all_bids_in = False

bids = {}


def do_bidding():
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bids[name] = int(bid)


def get_highest_bid():
    highest_bid = {"name": '', "bid": 0}

    for key in bids:
        if bids[key] > highest_bid.get("bid"):
            highest_bid['name'] = key
            highest_bid['bid'] = bids[key]

    return highest_bid


while not all_bids_in:
    do_bidding()

    continue_bidding = input(
        "Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if continue_bidding == 'no':
        all_bids_in = True

        highest_bid = get_highest_bid()

        print(f"The winner is {highest_bid['name']} with a bid of ${
              highest_bid['bid']}.")
    else:
        print("\n" * 20)
