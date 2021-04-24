

def is_prime(liczba):
    if liczba is 1:
        return True

    for l in range(2, liczba):
        if liczba % l == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(1) is True
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(17) is True
