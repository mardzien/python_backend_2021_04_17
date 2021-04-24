"""Napisz funkcję, która zliczy znaki pomiędzy określonymi znacznikami, dodając wagę zgodnie z poziomem zagnieżdżenia:

np. jeśli nasze znaczniki to <>, to:

policz_znaki("") == 0
policz_znaki("<>") == 0
policz_znaki("<a<bc>>") == 5
itd.

Możemy też podać inne znaczniki, wtedy:

policz_znaki("<>", start="[", stop="]") == 0

policz_znaki("[a<bcd>]") == 6"""


def policz_znaki(napis, start="<", stop=">"):

    flag = 0
    count = 0

    for letter in napis:
        if letter == start:
            flag += 1
        elif letter == stop:
            flag -= 1
        else:
            count += flag

    return count


print(policz_znaki("<>", start="[", stop="]"))
print(policz_znaki("[a<bcd>]", start="[", stop="]"))
print(policz_znaki("<a<bc>>"))
