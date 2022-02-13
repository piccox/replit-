#Solution and Complete Code for the Secret Auction Program

from replit import clear
#hint: call clear() to clear the output in the console. 

from art import logo
print(logo)


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  #bidding_record = {"mee":130,"soo":200}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
bidding_finished = False

while not bidding_finished:
  # put these to into while loop 
  name = input("What is your name?")
  # later on "name" will be a key
  price = int(input("what is your bid? $"))
  # and "price" is going to be the corresponding values 
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'Yes' or 'no'.")
  if should_continue == "no":
    bidding_finished = True
  elif should_continue == "yes":
    clear()



find_highest_bidder(bids)
   



