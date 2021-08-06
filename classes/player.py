# Class of player's info
class Player:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        # A new player has no cards
        self.all_cards = []
        # A new player has 0 amount
        self.amount = 0

    def add_amount(self, new_values):
        if new_values == 11:
            while True:
                try:
                    ace_amount = int(input('You have received Ace card, would you like to count it as 1 or 11?(Enter 1 or 11):'))
                except:
                    print('Looks like you did not enter an integer!')
                    continue
                else:
                    self.amount += ace_amount
                    break
        else:
            self.amount += new_values

    def add_cards(self, new_cards):
        self.all_cards.append(new_cards)

    def display_cards(self):
        print('Your cards: ', *self.all_cards, sep = '\n')

    def __str__(self):
        return (f"Player's name: {self.name}\nYour current money: {self.money}")
