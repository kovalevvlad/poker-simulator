from collections import Counter

from app.util import check_argument


class FiveCardHand:

    def __init__(self, cards):
        check_argument(len(cards) == 5, "A 5-card hands must have exactly 5 cards")
        check_argument(len(set(cards)) == 5, "All cards must be distinct in a 5-card hand")
        self.cards = cards

    def score(self):
        """
        an object which can be used to compare two hands.
        For any two hands a and b, a.score() > b.score() implies that hand a beats hand b.
        a.score() == b.score() implies that a and b are of equal strength.
        """

        # https://en.wikipedia.org/wiki/List_of_poker_hand_categories
        if self._is_flush() and self._is_straight():
            return 8, self._high_card_component()

        elif self._is_four_of_a_kind():
            return 7, self._rank_with_frequency(4), self._high_card_component()

        elif self._is_full_house():
            return 6, self._rank_with_frequency(3), self._rank_with_frequency(2)

        elif self._is_flush():
            return 5, self._high_card_component()

        elif self._is_straight():
            # Think about a low straight, the second card resolves this issue
            return 4, -1 if self._labeled_rank_histogram().has_key("A") else max(card.numeric_rank() for card in self._high_card_component())

        elif self._is_three_of_a_kind():
            return 3, self._rank_with_frequency(3)

        elif self._is_two_pair():
            return 2, list(sorted((rank for rank, count in self._labeled_rank_histogram().items() if count == 2), reverse=True)), self._high_card_component()

        elif self._is_pair():
            return 1, self._rank_with_frequency(2), self._high_card_component()

        else:
            return 0, self._high_card_component()

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
        return hand_string in "23456789TJQKA" or hand_string == "2345A"

    def _is_four_of_a_kind(self):
        return self._rank_histogram() == [1, 4]

    def _is_three_of_a_kind(self):
        return self._rank_histogram() == [1, 1, 3]

    def _rank_histogram(self):
        return sorted(self._labeled_rank_histogram().values())

    def _labeled_rank_histogram(self):
        return Counter(card.rank for card in self.cards)

    def _rank_with_frequency(self, frequency):
        return next(rank for rank, count in self._labeled_rank_histogram().items() if count == frequency)
