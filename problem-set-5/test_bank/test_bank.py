from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("hey") == 20


def test_noth():
    assert value("sup") == 100


def test_case():
    assert value("HELLO!") == 0
