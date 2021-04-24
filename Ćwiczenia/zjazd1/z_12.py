

def append(element, lista=None):

    if lista:
        return lista + [element]
    else:
        return [element]


# print(append(2, [4, 6]))
# print(append(2))


def test_append():
    assert append(5) == [5]
    assert append(4, [1, 2, 3]) == [1, 2, 3, 4]
