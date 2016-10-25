import pytest
from app.poker.deck import Deck

CARD_COUNT = 52


def test_exception_is_thrown_when_popping_empty_deck():
    with pytest.raises(Exception):
        Deck([]).pop()


def test_shuffling():
    ordered_ints = range(CARD_COUNT)
    deck = Deck(ordered_ints)
    deck.shuffle()
    shuffled_ints = [deck.pop() for x in range(CARD_COUNT)]
    assert shuffled_ints != ordered_ints and shuffled_ints != list(reversed(ordered_ints))


def test_popping():
    ordered_cards = range(CARD_COUNT)
    deck = Deck(ordered_cards)
    assert [deck.pop() for x in range(CARD_COUNT)] == list(reversed(ordered_cards))
