from collections import defaultdict

numbers = [1, 4, 5, 6, 8, 19, 34, 55]


def mod3(n): return n % 3


# def group_by(iterable, key_func=lambda x: x):
#
#     d = dict()
#
#     for element in iterable:
#         if not key_func(element) in d.keys():
#             d[key_func(element)] = [element]
#         else:
#             d[key_func(element)].append(element)
#
#     return d


def group_by(iterable, key_func=lambda x: x):

    d = defaultdict(list)

    for element in iterable:
        d[key_func(element)].append(element)

    return d


print(group_by(numbers, key_func=mod3))


print(group_by([1, 2, 1, 3, 2, 1]))
# wynik = "{1: [1, 1, 1], 2: [2, 2], 3: [3]}"

animals = [
        ('agatha', 'dog'),
        ('kurt', 'cat'),
        ('margaret', 'mouse'),
        ('cory', 'cat'),
        ('mary', 'mouse'),
    ]

print(group_by(animals, key_func=lambda x: x[1]))


def test_group_by():
    result = {
        'mouse': [('margaret', 'mouse'), ('mary', 'mouse')],
        'dog': [('agatha', 'dog')],
        'cat': [('kurt', 'cat'), ('cory', 'cat')],
    }

    assert group_by(numbers, key_func=mod3) == {0: [6], 1: [1, 4, 19, 34, 55], 2: [5, 8]}
    assert group_by([1, 2, 1, 3, 2, 1]) == {1: [1, 1, 1], 2: [2, 2], 3: [3]}
    assert group_by(animals, key_func=lambda x: x[1]) == result
