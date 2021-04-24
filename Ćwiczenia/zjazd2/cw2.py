"""
formatuj(
            "nazwa produktu: $name",
            "cena produktu: $price PLN",
            "stawka vat: $vat%"
            name="Ogórki",
            price=2.55,
            vat=15
        )
wynik:

nazwa produktu: Ogórki
cena produktu: 2.55 PLN
stawka vat: 15%
"""


def formatuj(*args, **kwargs):

    result = "\n".join(args)

    for k, v in kwargs.items():
        result = result.replace(f"${k}", str(v))

    return result


print(formatuj("nazwa produktu: $name", "cena produktu: $price PLN", "stawka vat: $vat%",
               name="Ogórki", price=2.55, vat=15))
