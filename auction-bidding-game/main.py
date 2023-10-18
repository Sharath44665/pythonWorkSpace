print("welcome to Auction program")
name = input("Whats your Name: ")
bid = int(input("Whats your Bid: $"))
anyBiddersExist = input("are there any bidders exist? type Yes or No:").lower()

def addBidders(name, bid, allBidders=[]):

    allBidders.append(
        {
            "name":name,
            "bid": bid,
        })

    return allBidders

def findWinner(allBidders):
    maxBid = float("-inf")
    winnerName = ""
    winnerMoney = 0
    # print(allBidders)

    for bidder in allBidders:

        for key in bidder:
            if key == "bid" and bidder[key] > maxBid:
                # print(f"currentVal: {bidder[key]},maxbid: {maxBid}")
                maxBid = bidder[key]
                winnerMoney = bidder[key]
                winnerName = bidder["name"]
    print(f"winner is {winnerName} won: ${winnerMoney} ")

print("----------------------")
allBids = 9
if anyBiddersExist == "no" or anyBiddersExist == "n":
    allBidders = addBidders(name=name, bid=bid)

    findWinner(allBidders=allBidders)
else:
    allBids = addBidders(name=name, bid= bid)

while anyBiddersExist == "yes" or anyBiddersExist == "y":
    name = input("Whats your Name: ")
    bid = int(input("Whats your Bid: $"))
    allBids = addBidders(name = name, bid = bid, allBidders=allBids)
    anyBiddersExist = input("are there any bidders exist? type Yes or No:").lower()
    print("----------------------")

    if anyBiddersExist == "no" or anyBiddersExist =="n":
        findWinner(allBidders = allBids)


