import pytest

from app.poker import simulator
from app.poker.card import Card


def test_simulator_sanity():
    # No chance of losing with the highest royal flush
    assert 1.0 == simulator.probability_of_winning(
        [Card("D", "A"), Card("D", "K")],
        3,
        [Card("D", "Q"), Card("D", "J"), Card("D", "T"), Card("H", "A"), Card("H", "9")])

    # No chance of winning with 2 and 3 as highest cards
    assert 0.0 == simulator.probability_of_winning(
        [Card("H", "2"), Card("D", "3")],
        3,
        [Card("H", "T"), Card("H", "A"), Card("D", "5"), Card("C", "J"), Card("C", "9")])

    # no certainty, want this to be close to 50% to avoid failures due to inaccurate answers being 1 or 0
    chance_of_winning = simulator.probability_of_winning(
        [Card("D", "T"), Card("H", "7")],
        3,
        [Card("H", "T"), Card("H", "A"), Card("D", "5"), Card("C", "J"), Card("C", "9")])
    assert chance_of_winning not in (1.0, 0.0)


def test_hand_must_have_two_cards():
    available_cards = [Card("H", "2"), Card("H", "3"), Card("H", "4")]
    for i in [0, 1, 3]:
        with pytest.raises(AssertionError) as exception:
            simulator.probability_of_winning(
                available_cards[:i],
                3,
                [Card("H", "T"), Card("H", "A"), Card("D", "5"), Card("C", "J"), Card("C", "9")])

            assert "hand" in str(exception)


def test_table_must_have_the_right_number_of_cards():
    available_cards = [Card("H", "T"), Card("H", "A"), Card("D", "5"), Card("C", "J"), Card("C", "9"), Card("D", "T")]
    for i in [1, 2, 6]:
        with pytest.raises(AssertionError) as exception:
            simulator.probability_of_winning(
                [Card("H", "2"), Card("H", "3")],
                3,
                available_cards[:i])

            assert "table" in str(exception)


def test_must_have_between_one_and_twentythree_opponents():
    for i in [0, 24]:
        with pytest.raises(AssertionError) as exception:
            simulator.probability_of_winning(
                [Card("H", "2"), Card("H", "3")],
                i,
                [Card("H", "T"), Card("H", "A"), Card("D", "5"), Card("C", "J"), Card("C", "9")])

            assert "opponents" in str(exception)
