from random import shuffle


class Deck:

    def __init__(self, cards):
        self.cards = list(cards)

    def shuffle(self):
        shuffle(self.cards)

    def pop(self):
        return self.cards.pop()
