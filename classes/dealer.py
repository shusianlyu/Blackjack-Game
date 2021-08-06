from player import Player
# Class of automated dealer
class Dealer(Player):

    def __init__(self):
        self.all_cards = []
        self.amount = 0

    def display_cards(self):
        print("Dealer's cards: ", *self.all_cards, sep = '\n' )

    def add_amount(self, new_values):
        self.amount += new_values

    def __str__(self):
        return f"Dealer's first card:\n{self.all_cards[0]}"
