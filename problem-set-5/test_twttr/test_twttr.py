from twttr import shorten


def test_upper():
    assert shorten("TWITTER") == "TWTTR"


def test_lower():
    assert shorten("twitter") == "twttr"


def test_mixed():
    assert shorten("TwiTtEr") == "TwTtr"


def test_numeric():
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("twitter!!") == "twttr!!"
