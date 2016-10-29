import pytest
from app.poker.card import Card


def test_exception_thrown_with_bad_suit():
    with pytest.raises(ValueError) as exception:
        Card("X", "K")
        assert "suit" in str(exception.value)


def test_exception_thrown_with_bad_rank():
    with pytest.raises(ValueError) as exception:
        Card("H", "X")
        assert "rank" in str(exception.value)


def test_numeric_ranks_monotonicity():
    ranks = "23456789TJQKA"
    numeric_ranks = [Card("H", r).numeric_rank() for r in ranks]
    assert all(larger > smaller for larger, smaller in zip(numeric_ranks[1:], numeric_ranks))


def test_equality():
    assert Card("H", "A") == Card("H", "A")
    assert Card("H", "A") != Card("C", "A")
    assert Card("H", "A") != Card("H", "T")


def test_hash():
    assert Card("H", "A").__hash__() == Card("H", "A").__hash__()
    assert Card("H", "A").__hash__() != Card("C", "A").__hash__()
    assert Card("H", "A").__hash__() != Card("H", "T").__hash__()


def test_lt():
    assert Card("C", "K") < Card("C", "A")


def test_gt():
    assert Card("C", "A") > Card("C", "K")
