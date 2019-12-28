from nsc import Handler

# Tests


def test_handler_create():
    object = Handler()
    assert isinstance(object, Handler)