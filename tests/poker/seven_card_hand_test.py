import pytest

from app.poker.card import Card
from app.poker.seven_card_hand import SevenCardHand
import random


def test_seven_card_hand_must_be_initialised_with_seven_cards():
    for i in [0, 1, 6, 8]:
        with pytest.raises(AssertionError):
            SevenCardHand(range(i))


def test_five_card_hand_must_be_initialised_with_distinct_items():
    with pytest.raises(AssertionError):
        SevenCardHand([1, 2, 3, 4, 5, 6, 6])


def test_best_five_card_subhand():
    best_subhand_cards = [Card("C", "J"),
                          Card("C", "T"),
                          Card("C", "9"),
                          Card("C", "8"),
                          Card("C", "7")]

    seven_cards = best_subhand_cards + [Card("H", "8"), Card("D", "A")]
    # in case order matters somehow
    random.shuffle(seven_cards)

    assert set(SevenCardHand(seven_cards).best_five_card_subhand().cards) == set(best_subhand_cards)
