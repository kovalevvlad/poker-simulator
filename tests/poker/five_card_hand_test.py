import pytest
from app.poker.five_card_hand import FiveCardHand
from app.poker.card import Card


def test_hand_scoring():
    raw_hands_in_winning_order = [
        ["CJ", "CT", "C9", "C8", "C7"],  # Straight flush
        ["C5", "D5", "H5", "S5", "D2"],  # Four of a kind
        ["S6", "H6", "D6", "CK", "HK"],  # Full house
        ["DJ", "D9", "D8", "D7", "D6"],  # Flush
        ["DT", "S9", "H8", "D7", "C6"],  # Straight
        ["CQ", "SQ", "HQ", "H7", "S6"],  # Three of a kind
        ["HJ", "SJ", "C3", "S3", "H2"],  # Two pair
        ["ST", "HT", "S8", "H7", "C4"],  # One pair
        ["DK", "DQ", "S7", "S4", "H3"]   # High card
    ]

    hands_in_winning_order = [FiveCardHand([Card(raw_card[0], raw_card[1]) for raw_card in rh]) for rh in raw_hands_in_winning_order]
    hand_scores_in_winning_order = [hand.score() for hand in hands_in_winning_order]
    assert all(higher_score < lower_score for higher_score, lower_score in zip(hands_in_winning_order, hand_scores_in_winning_order[:1]))


def test_five_card_hand_must_be_initialised_full():
    with pytest.raises(ValueError):
        FiveCardHand([1, 2, 3, 4])


def test_five_card_hand_must_be_initialised_with_distinct_items():
    with pytest.raises(ValueError):
        FiveCardHand([1, 2, 3, 4, 4])


def test_high_card_does_the_job():
    best_straight_flush = [Card("C", rank) for rank in "AKQJT"]
    next_best_straight_flush = [Card("C", rank) for rank in "KQJT9"]
    assert FiveCardHand(best_straight_flush).score() > FiveCardHand(next_best_straight_flush).score()


def test_strongest_pair_wins():
    weaker_hand = FiveCardHand([Card("H", "A"), Card("C", "K"), Card("S", "Q"), Card("C", "3"), Card("H", "3")])
    stronger_hand = FiveCardHand([Card("H", "A"), Card("S", "K"), Card("C", "K"), Card("S", "7"), Card("H", "6")])
    assert weaker_hand.score() < stronger_hand.score()


def test_strongest_two_pair_wins():
    stronger_hand = FiveCardHand([Card("H", "T"), Card("C", "T"), Card("S", "6"), Card("C", "6"), Card("H", "3")])
    weaker_hand = FiveCardHand([Card("H", "A"), Card("S", "9"), Card("C", "9"), Card("S", "7"), Card("H", "7")])
    assert weaker_hand.score() < stronger_hand.score()


def test_strongest_full_house_wins():
    weaker_hand = FiveCardHand([Card("H", "T"), Card("C", "T"), Card("S", "6"), Card("C", "6"), Card("H", "6")])
    stronger_hand = FiveCardHand([Card("H", "7"), Card("S", "7"), Card("C", "7"), Card("S", "2"), Card("H", "2")])
    assert weaker_hand.score() < stronger_hand.score()


def test_low_straight_loses_to_regular_straight():
    stronger_hand = FiveCardHand([Card("H", "2"), Card("C", "3"), Card("S", "4"), Card("C", "5"), Card("H", "6")])
    weaker_hand = FiveCardHand([Card("H", "A"), Card("S", "2"), Card("C", "3"), Card("S", "4"), Card("H", "5")])
    assert weaker_hand.score() < stronger_hand.score()


def test_low_straight():
    weaker_hand = FiveCardHand([Card("H", "A"), Card("C", "A"), Card("S", "4"), Card("C", "5"), Card("H", "6")])
    stronger_hand = FiveCardHand([Card("H", "A"), Card("S", "2"), Card("C", "3"), Card("S", "4"), Card("H", "5")])
    assert weaker_hand.score() < stronger_hand.score()
