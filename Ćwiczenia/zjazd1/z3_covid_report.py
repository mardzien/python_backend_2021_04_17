wojewodztwa = """
Kraj
dolnośląskie
kujawsko-pomorskie
lubelskie
lubuskie
łódzkie
małopolskie
mazowieckie
opolskie
podkarpackie
podlaskie
pomorskie
śląskie
świętokrzyskie
warmińsko-mazurskie
wielkopolskie
zachodniopomorskie"""

przypadki="""
21130
2277
1085
892
505
1300
1747
2555
638
923
374
1008
3142
659
520
2495
824"""

zgony="""
682
46
33
21
18
63
36
93
15
59
17
22
93
50
12
80
24"""

wojewodztwa = wojewodztwa.split("\n")[1:]
przypadki = przypadki.split("\n")[1:]
zgony = zgony.split("\n")[1:]

for w, p, z in zip(wojewodztwa, przypadki, zgony):
    print(f"{w:20} {p:10} {z:10} {(int(z)/ int(p) * 100):2f}")
