def czy_przysta(liczba):
    return liczba % 2 == 0


def test_czy_parzysta_dla_l_parzystej():
    assert czy_przysta(2) is True


def test_czy_parzysta_dla_l_nieparzystej():
    assert czy_przysta(3) is False