from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("hello, GEM") == 0
    assert value("hey") == 20
    assert value("What's happening?") == 100
