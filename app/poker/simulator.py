from collections import Counter

from card import Card
from deck import Deck
from seven_card_hand import SevenCardHand

_ITERATIONS = 1000


def probability_of_winning(my_hand, opponent_count, table_cards):

    assert len(my_hand) == 2, "A player's hand must have 2 cards exactly"
    assert len(table_cards) in (0, 3, 4, 5), "A table can only have 0, 3, 4 or 5 cards at any given time"
    assert 0 < opponent_count < 23, "The number of opponents must be between 1 and 23, inclusive"

    duplicated_cards = [card for card, count in Counter(my_hand + table_cards).items() if count > 1]
    assert len(duplicated_cards) == 0, "The following cards appeared multiple times in table_cards + players_hand - {}".format(",".join(duplicated_cards))

    all_cards = {Card(suit, rank) for suit in "HDSC" for rank in "23456789TJQKA"}
    undealt_cards = list(all_cards - set(my_hand + table_cards))

    my_wins = 0
    for i in xrange(_ITERATIONS):
        remaining_deck = Deck(undealt_cards)
        remaining_deck.shuffle()

        opponents_small_hands = [[remaining_deck.pop(), remaining_deck.pop()] for i in xrange(opponent_count)]

        full_table_size = 5
        full_table = table_cards + [remaining_deck.pop() for i in xrange(full_table_size - len(table_cards))]

        my_best_five_card_hand = SevenCardHand(full_table + my_hand).best_five_card_subhand()
        opponents_seven_card_hands = [SevenCardHand(opponent_small_hand + full_table) for opponent_small_hand in opponents_small_hands]
        opponents_best_five_card_hands = [seven_card_hand.best_five_card_subhand() for seven_card_hand in opponents_seven_card_hands]
        best_opponent_five_card_subhand_of_all = max(opponents_best_five_card_hands, key=lambda hand: hand.score())

        if my_best_five_card_hand.score() > best_opponent_five_card_subhand_of_all.score():
            my_wins += 1

    return float(my_wins) / float(_ITERATIONS)
