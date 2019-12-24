from nsc.deck import Deck
from nsc.hand import Hand

# Tests


def test_deck_create():
    object = Deck()
    assert isinstance(object, Deck)
    assert len(object.deck) == 56
    assert object.deck[0] == "King"
    assert object.deck[55] == "Same"
    assert object.draw == []
    assert list(object.hands.keys()) == ["White", "Black"]
    assert isinstance(object.hands["White"], Hand)
    assert isinstance(object.hands["Black"], Hand)


