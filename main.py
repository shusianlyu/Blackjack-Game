from blackjack_game import BlackjackGame
from card import Card
from dealer import Dealer
from player import Player
from deck import Deck

def main():
    name = input('Enter your name: ')
    total_money = 100  # starting money
    blackjack = BlackjackGame()

    play_again = True
    while play_again:

        blackjack.welcome()

        # Create and shuffle the deck
        mydeck = Deck()
        mydeck.shuffle()

        # Create a Player and the dealer
        player = Player(name, total_money)
        dealer = Dealer()

        # Display player's name and current money
        print(player)

        # if the play is bankrupt, Preventing the player from playing
        if player.money == 0:
            print('You are bankrupt!')
            break

        # taking bet
        betting_amount = blackjack.take_bet(player)

        # Distribute two cards to the player and automated dealer
        for x in range(2):
            player.add_cards(mydeck.distribute_one())
            dealer.add_cards(mydeck.distribute_one())

        # print first card of the dealer
        print(dealer)

        # Display player's cards
        player.display_cards()

        # Calculate sum of first two cards of dealer and player
        for cards in dealer.all_cards:
            dealer.add_amount(cards.value)
        for cards in player.all_cards:
            player.add_amount(cards.value)

        game_on = True

        # Check if game on
        while game_on:

            # Ask player if wanted more cards
            game_on = blackjack.hit_or_stand(player, dealer, mydeck)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.amount > 21:
                blackjack.player_busts(player, betting_amount)
                break

        # after player's turn, check who wins the game
        if player.amount <= 21:
            if dealer.amount >= 17:
                dealer.display_cards()
            while dealer.amount < 17:
                print('Add one more card to dealer!')
                dealer.add_cards(mydeck.distribute_one())
                dealer.display_cards()
                dealer.add_amount(dealer.all_cards[-1].value)

            # Display final cards and sum
            player.display_cards()
            print(f'Sum of dealer: {dealer.amount}')
            print(f'Sum of you: {player.amount}')

            # Run different scenarios
            if dealer.amount > 21:
                blackjack.dealer_busts(player, betting_amount)

            elif dealer.amount > player.amount:
                blackjack.dealer_wins(player, betting_amount)

            elif dealer.amount < player.amount:
                blackjack.player_wins(player, betting_amount)

            else:
                blackjack.tie()

        # update player's money
        total_money = player.money

        # update if playing again
        while True:
            keep_playing = input("Play again('Y' or 'N')? ")
            if keep_playing.upper() == 'N':
                play_again = False
                print('Thank you for your participation!\nWe will see you very soon😊')
                break
            elif keep_playing.upper() == 'Y':
                break
            else:
                print('Looks like you did not type Y or N, please enter again!')
                continue

if __name__ == '__main__':
    main()
