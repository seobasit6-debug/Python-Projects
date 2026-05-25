print("""
     _____________
          /
     )_______(
     |""|""|""|_.-._.-._.-.
     |         | |  |         | |''-.
     |         |_|  |_        _| |_.-'
     |_________|  '-'``-----''  '-'
     )""|""|""(
     /_________ \\
      .-----------. 
     /______________\\
""")

bidders = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    more = input("Are there any other bidders? Type 'yes' or 'no'.\n  ")
    if more.lower() == "no":
        break

winner = max(bidders, key=bidders.get)
print(f"The winner is {winner} with a bid of ${bidders[winner]}")