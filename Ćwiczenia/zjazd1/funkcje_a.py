def add(a, b):
    return a + b


def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(-10, -8) == -18
