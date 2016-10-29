import itertools

from five_card_hand import FiveCardHand
from app.util import check_argument


class SevenCardHand:

    def __init__(self, cards):
        check_argument(len(cards) == 7, "A 7-card hands must have exactly 7 cards")
        check_argument(len(set(cards)) == 7, "All cards must be distinct in a 7-card hand")
        self.cards = cards

    def best_five_card_subhand(self):
        all_five_card_subhands = [FiveCardHand(five_cards) for five_cards in itertools.combinations(self.cards, 5)]
        return max(all_five_card_subhands, key=lambda hand: hand.score())
