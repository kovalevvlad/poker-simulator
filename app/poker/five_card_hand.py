from collections import Counter


class FiveCardHand:

    def __init__(self, cards):
        assert len(cards) == 5, "A 5-card hands must have exactly 5 cards"
        assert len(set(cards)) == 5, "All cards must be distinct in a 5-card hand"
        self.cards = cards

    def score(self):
        """
        an object which can be used to compare two hands.
        For any two hands a and b, a.score() > b.score() implies that hand a beats hand b.
        a.score() == b.score() implies that a and b are of equal strength.
        """

        # https://en.wikipedia.org/wiki/List_of_poker_hand_categories
        hand_type_matches = [
            self._is_flush() and self._is_straight(),   # Straight flush
            self._is_four_of_a_kind(),                  # Four of a kind
            self._is_full_house(),                      # Full house
            self._is_flush(),                           # Flush
            self._is_straight(),                        # Straight
            self._is_three_of_a_kind(),                 # Three of a kind
            self._is_two_pair(),                        # Two pair
            self._is_pair(),                            # One pair
            True]                                       # High card

        best_available_hand_category = [category_index for category_index, category_matches in enumerate(reversed(hand_type_matches)) if category_matches][-1]
        return best_available_hand_category, self._high_card_component()

    def _is_flush(self):
        return len(set(card.suit for card in self.cards)) == 1

    def _is_full_house(self):
        return self._rank_histogram() == [2, 3]

    def _high_card_component(self):
        return sorted(self.cards, key=lambda card: card.numeric_rank(), reverse=True)

    def _is_pair(self):
        return self._rank_histogram() == [1, 1, 1, 2]

    def _is_two_pair(self):
        return self._rank_histogram() == [1, 2, 2]

    def _is_straight(self):
        ranks_in_order = list(card.rank for card in sorted(self.cards, key=lambda card: card.numeric_rank()))
        hand_string = "".join(ranks_in_order)
        return hand_string in "A23456789TJQKA"

    def _is_four_of_a_kind(self):
        return self._rank_histogram() == [1, 4]

    def _is_three_of_a_kind(self):
        return self._rank_histogram() == [1, 1, 3]

    def _rank_histogram(self):
        return sorted(Counter(card.rank for card in self.cards).values())
