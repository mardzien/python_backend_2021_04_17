

napis = "ala ma kota a kot ma ale"

d = {}

for letter in napis:
    if not d.get(letter):
        d[letter] = 1
    else:
        d[letter] += 1

print(d)


d1 = {}

for letter in napis:
    if letter not in list(d1.keys()):
        d1[letter] = 1
    else:
        d1[letter] += 1

print(d1)
