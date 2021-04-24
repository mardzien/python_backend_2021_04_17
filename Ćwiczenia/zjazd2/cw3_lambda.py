

imiona = ["Rafał", "Ada", "Alcybiades", "Korfanty", "Zenobia", "Krzysztof", "Krystyna", "Robert"]


def sort_names(names):

    result = sorted(names, key=lambda x: len(x))
    result = sorted(result, key=lambda x: x[0])

    return result


print(sort_names(imiona))
