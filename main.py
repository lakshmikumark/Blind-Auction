from replit import clear
#HINT: You can call clear() to clear the output in the console.

bidders_list = []

def new_bidder():
  name = input("Please enter your name: ")
  bid = input("\nPlease enter your bid: $")
  new_bid = {}
  new_bid["name"] = name
  new_bid["bid"] = bid
  bidders_list.append(new_bid)



def highest_bidder():
  prev_bid = 0
  for bidders_dict in bidders_list:
    if int(bidders_dict["bid"]) > int(prev_bid):
      highest_bid = bidders_dict["bid"]
      prev_bid = highest_bid

  for bidders_dict in bidders_list:
    if bidders_dict["bid"] == highest_bid:
      print("Highest bidder is " + bidders_dict["name"])

more_bidders = 'Yes'
while(more_bidders == 'Yes'):
  more_bidders = input("\nAre there any other bidders?")
  if more_bidders == 'Yes':
    clear()
    new_bidder()
  else:
    highest_bidder()
