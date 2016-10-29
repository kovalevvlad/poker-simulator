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
