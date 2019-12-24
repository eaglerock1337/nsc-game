from nsc.deck import Deck

# Tests


def test_deck_create():
    object = Deck()
    assert len(object.deck) == 56
    assert object.deck[0] == "King"
    assert object.deck[55] == "Same"