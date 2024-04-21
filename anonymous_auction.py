import os


def find_winner(bidders_list):
    highest_bid = 0
    winner = ' '
    for bidder in bidders_list:
        bidders_price = bidders_list[bidder]
        if bidders_price > highest_bid:
            highest_bid = bidders_price
            winner = bidder
    print(f'The winner of the bid is {winner} with a bid price of  {highest_bid}')


auction_info = {}
end_auction = False
while not end_auction:
    name = input('What is your name? : ')
    bid_amount = int(input('How much are you bidding? : '))
    i = name
    auction_info[i] = bid_amount
    another_bidder = input('Is there another bidder? (yes/no) : ')
    if another_bidder.lower() == 'no':
        end_auction = True
        find_winner(auction_info)
    elif another_bidder.lower() == 'yes':
        os.system('cls')
        continue
    else:
        print('Invalid input')
