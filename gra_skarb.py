import random


x_gracza = random.randint(1, 10)
y_gracza = random.randint(1, 10)

x_skarbu = random.randint(1, 10)
y_skarbu = random.randint(1, 10)


while x_gracza == x_skarbu and y_gracza == y_skarbu:
    x_gracza = random.randint(1, 10)
    y_gracza = random.randint(1, 10)

    x_skarbu = random.randint(1, 10)
    y_skarbu = random.randint(1, 10)

counter = 0

max_liczba_krokow = 2 * (abs(x_gracza - x_skarbu) + abs(y_skarbu - y_gracza))

while True:

    print(f"Twoje współrzędne to x: {x_gracza}, y: {y_gracza}.")

    odleglosc_przed = abs(x_gracza - x_skarbu) + abs(y_skarbu - y_gracza)

    ruch = input("""
    Wpisz:
    a - żeby poruszyć się w lewo
    d - żeby poruszyś się w prawo
    w - żeby poruszyś się w górę
    s - żeby poruszyś się w dół
    """)

    counter += 1

    if ruch == "a":
        x_gracza -= 1
    elif ruch == "d":
        x_gracza += 1
    elif ruch == "w":
        y_gracza += 1
    elif ruch == "s":
        y_gracza -= 1
    else:
        print("Błędna komenda!")
        continue

    if x_gracza < 1 or x_gracza > 10 or y_gracza < 1 or y_gracza > 10:
        print("Wypadłeś poza planszę!")
        break

    if x_gracza == x_skarbu and y_gracza == y_skarbu:
        print(f"Znalazłeś skarb. Liczba ruchów: {counter}")
        break

    odleglosc_po = abs(x_gracza - x_skarbu) + abs(y_skarbu - y_gracza)

    if odleglosc_po < odleglosc_przed:
        print("Zbliżasz się do skarbu")
    else:
        print("Oddalasz się od skarbu")

    if counter > max_liczba_krokow:
        print("Położenie skarbu się zmienia.")

        x_skarbu = random.randint(1, 10)
        y_skarbu = random.randint(1, 10)

        counter = 0
        max_liczba_krokow = 2 * (abs(x_gracza - x_skarbu) + abs(y_skarbu - y_gracza))
