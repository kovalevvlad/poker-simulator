# hearts, diamonds, clubs and spades
from functools import total_ordering

from app.util import check_argument

_SUITS = 'HDCS'
_RANKS = '23456789TJQKA'


@total_ordering
class Card:

    def __init__(self, suit, rank):

        check_argument(suit in _SUITS, "Suit was {} but must be one of '{}'".format(suit, ','.join(_SUITS)))
        check_argument(rank in _RANKS, "Rank was {} must be one of '{}'".format(rank, ','.join(_RANKS)))

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def __repr__(self):
        return str(self)

    def numeric_rank(self):
        return _RANKS.index(self.rank)

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash((self.suit, self.rank))

    def __lt__(self, other):
        return self.numeric_rank() < other.numeric_rank()
