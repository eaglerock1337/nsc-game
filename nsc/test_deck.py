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


def test_deck_set_difficulty():
    object = Deck()
    object.set_difficulty(2)
    assert object.difficulty == 2


def test_deck_shuffle():
    result = ["Queen", "Pawn", "King", "Pawn", "Rook"]
    object = Deck()
    object.draw = ["Queen"]
    object.hands["White"].discards = ["Pawn", "King", "Knight"]
    object.hands["Black"].discards = ["Pawn", "Rook", "Bishop"]
    object.shuffle()
    assert set(object.draw) == set(result)


def test_deck_new_game():
    object = Deck()
    object.new_game()
    assert object.deck != object.draw
    assert set(object.deck).difference(object.draw) == set()


def test_deck_draw_card():
    object = Deck()
    object.draw = ["Queen", "Pawn", "King", "Pawn", "Rook"]
    object.draw_card("White")
    object.draw_card("Black")
    object.draw_card("Black")
    assert object.draw == ["Queen", "Pawn"]
    assert object.hands["White"].cards == ["Rook"]
    assert object.hands["Black"].cards == ["Pawn", "King"]