from nsc import Hand

# Tests


def test_hand_create():
    object = Hand()
    assert object.cards == []
    assert object.discards == []


def test_hand_add_card():
    object = Hand()
    object.add_card("King")
    object.add_card("Queen")
    object.add_card("Pawn")
    assert object.cards == ["King", "Queen", "Pawn"]


def test_hand_discard():
    object = Hand()
    object.cards = ["King", "Queen", "Pawn", "Queen"]
    assert object.cards == ["King", "Queen", "Pawn", "Queen"]
    object.discard("Queen")
    assert object.cards == ["King", "Pawn", "Queen"]
    assert object.discards == ["Queen"]
    object.discard("King")
    assert object.cards == ["Pawn", "Queen"]
    assert object.discards == ["Queen", "King"]


def test_hand_discard_hand():
    hand = ["King", "Queen", "Pawn", "Queen"]
    object = Hand()
    object.cards = hand
    object.discard_hand()
    assert len(object.cards) == 0
    assert len(object.discards) == 4


def test_hand_get_cards():
    expected = {
        "King": 1,
        "Queen": 2,
        "Pawn": 1,
    }
    object = Hand()
    object.cards = ["King", "Queen", "Pawn", "Queen"]
    result = object.get_cards()
    assert expected == result


def test_hand_get_discard():
    object = Hand()
    object.cards = ["King", "Queen", "Pawn", "Queen"]
    assert object.get_discard() is None
    object.discard("Queen")
    assert object.get_discard() == "Queen"
    object.discard("Pawn")
    assert object.get_discard() == "Pawn"


def test_hand_shuffle_discards():
    object = Hand()
    object.discards = ["King", "Queen", "Pawn", "Queen"]
    result = object.shuffle_discards()
    assert object.discards == ["Queen"]
    assert result == ["King", "Queen", "Pawn"]


def test_hand_reset():
    object = Hand()
    object.cards = ["King", "Queen", "Pawn", "Queen"]
    object.discard("Queen")
    object.discard("Pawn")
    object.reset()
    assert object.cards == []
    assert object.discards == []
