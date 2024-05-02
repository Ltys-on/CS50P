from plates import is_valid


def test_two():
    assert is_valid("A1") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False


def test_middlenumbers():
    assert is_valid("AA123A") == False


def test_zero():
    assert is_valid("AAA012") == False


def test_punctuation():
    assert is_valid("AA!!") == False