

liczby = [5, 2, 1, 4, 3]

print(liczby.index(min(liczby)))
print(id(liczby))


def zamien_min_max(lista):

    lista = lista[:]
    print(id(lista))

    index_min = lista.index(min(lista))
    index_max = lista.index(max(lista))

    temp_min = min(lista)
    temp_max = max(lista)

    lista[index_min] = temp_max
    lista[index_max] = temp_min

    return lista


print(zamien_min_max(liczby))

# assert liczby == [1, 2, 5, 4, 3]
print(liczby)


min_v = 0
max_v = 0

for x in range(len(liczby)):
    pass