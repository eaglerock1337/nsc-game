from nsc import Core, Handler

# Tests


def test_core_create():
    handler = Handler()
    object = Core(handler)
    assert isinstance(object, Core)
    assert isinstance(object.handler, Handler)
    assert object.difficulty == 1


def test_core_set_difficulty():
    handler = Handler()
    object = Core(handler)
    object.set_difficulty(2)
    assert object.difficulty == 2
    assert object.hand_size == 3


def test_core_new_game():
    handler = Handler()
    object = Core(handler)
    object.new_game()
    assert len(object.deck.draw) == 56
    assert len(object.deck.hands["White"].cards) == 0
    object.set_difficulty(3)
    object.new_game()
    assert len(object.deck.draw) == 46
    assert len(object.deck.hands["Black"].cards) == 5


def test_core_take_turn():
    pass