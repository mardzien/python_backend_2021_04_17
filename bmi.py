

def oblicz_bmi():
    imie = input("Podaj imię: ")
    wzrost = float(input("Podaj wzrost: "))
    waga = float(input("Podaj wagę: "))

    bmi = waga / wzrost ** 2

    d = {
        'imię: ': imie,
        'wzrost: ': wzrost,
        'waga: ': waga,
        'bmi: ': bmi,
    }

    for k, v in d.items():

        if isinstance(v, str):
            print(f"{k:<10} {v:>10}")
        else:
            print(f"{k:<10} {v:>10.2f}")


oblicz_bmi()
