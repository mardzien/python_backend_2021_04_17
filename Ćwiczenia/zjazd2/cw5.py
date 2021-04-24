from functools import partial


def incr_factory(liczba1):
    def dodawanie(liczba2):
        return liczba1 + liczba2
    return dodawanie


incr10 = incr_factory(10)

print(incr10(11))


def incr_factory2(liczba1, liczba2): return liczba1 + liczba2


incr20 = partial(incr_factory2, 20)
print(incr20(8))
