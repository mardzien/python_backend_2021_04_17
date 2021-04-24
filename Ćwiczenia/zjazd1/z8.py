def get_bigger(a, b):
    if a > b:
        return a
    else:
        return b


def max_of_three(a, b, c):

    z = get_bigger(a, b)
    result = get_bigger(z, c)

    return result


def test_max_of_three():
    assert max_of_three(1, 4, 16) == 16
    assert max_of_three(-1, -4, -16) == -1
    assert max_of_three(0, -4, -16) == 0
