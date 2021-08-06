class BlackjackGame():

    def welcome(self):
        print("Welcome to BlackJack! Try to bet the dealer's hand without going over 21!\n")

    def hit_or_stand(self, player, dealer, mydeck):
        global game_on

        while True:
            more_cards = input("\nMore cards('Hit' or 'Stand')? ")
            if more_cards.title() == "Hit":
                # if player wants more cards, give the player one more card and display player's current card list
                player.add_cards(mydeck.distribute_one())
                player.display_cards()
                player.add_amount(player.all_cards[-1].value)
                game_on = True
            elif more_cards.title() == 'Stand':
                print(f"Your turn has ended! It is dealer's turn!\n")
                game_on = False
            else:
                print('Sorry, please try again!')
                continue
            break
        return game_on

    # function to take bet
    def take_bet(self, player):
        while True:
            # Letting players pick their betting amount
            try:
                betting_amount = int(input('Pick your betting amount: '))
                print('\n')
            except:
                print('Looks like you did not enter an integer, please enter again!')
                continue
            else:
                if player.money < betting_amount:
                    print('Your betting amount can not be greater than your total amount of money!')
                    continue
                else:
                    return betting_amount
                    break

    # function for calculating remaining bet
    def win_bet(self, player, betting_amount):
        print(f'You have won {round(1.5*betting_amount)}')
        player.money += round(1.5 * (betting_amount))
        print(f'Your money: {player.money}')

    def lose_bet(self, player, betting_amount):
        player.money -= betting_amount
        print(f'Your money: {player.money}')

    # Game result scenarios
    def player_busts(self, player, betting_amount):
        print(f'Your sum: {player.amount}')
        print (f'You bust! Game over! You have lost {betting_amount}')
        self.lose_bet(player, betting_amount)

    def player_wins(self, player, betting_amount):
        print('Dealer has reached 17 but not passed your hand! You win!!')
        self.win_bet(player, betting_amount)

    def dealer_wins(self, player, betting_amount):
        print(f'Dealer has passed your sum but not passing 21! You lost your betting amount: {betting_amount}')
        self.lose_bet(player, betting_amount)

    def dealer_busts(self, player, betting_amount):
        print('Dealer busts! You win!!')
        self.win_bet(player, betting_amount)

    def tie(self):
        print("Dealer and Player tie! It's a push.")
