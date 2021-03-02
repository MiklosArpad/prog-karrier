
"""Feladat: Hány hétig kell lottóznunk az ötösért?
            Szimuláljon le egy ötös lottó húzási folyamatot.
            (1:43 949 268 -  telitalálat
            1:103 410 - négy találat
            1:1 231 - három találat
            1.45 - kettö találat"""

import random

eredmenyek = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0}
#telitalalat = False
hetek_szama = 0
talalaltok_szama = 0

"""Ez egy heti lootóhúzás függvénye"""

while talalaltok_szama <4:
    hetek_szama += 1
    """A sample függvénynek megadható neki egy intervallum itt a range mondja meg neki a terület nagyságát"""
    tipp = random.sample(range(1, 91), k=5)
    nyeroszamok = random.sample(range(1, 91), k=5)

    """A listák átalakítása halmazzá és a kettő metszetét veszi nyerőszámoknak  - közös elemek listája -"""

    talalaltok_szama = len(set(tipp) & set(nyeroszamok))

    """"1-gyel növeljük az eredmények számát a 0 kezdőértékhez"""
    eredmenyek[talalaltok_szama] += 1
    if talalaltok_szama == 3:
        print("Eltelt hetek száma:", hetek_szama)

#print(eredmenyek)
print("Eltelt évek száma:", hetek_szama//52)
for i in  range(6):
    print(i, "találat:", round(eredmenyek[i]/hetek_szama*100, 4), "%")
    if eredmenyek[i] > 0:
        print("\tArány: 1 /", round(1/(eredmenyek[i]/hetek_szama), 2))