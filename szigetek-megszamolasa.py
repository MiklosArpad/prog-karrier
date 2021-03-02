"""Feladat: Számolja meg a szigeteket egy két dimenziós tömben.
            ' ' = víz, 'x' = föld, a tömböt víz veszi körül.
            Bónusz feladat: rajzolja is ki a sziget térképét.
            (Google)"""

import random
import copy

MERET = 10
terkep = [random.choices((' ', 'x'), k=MERET) for i in range(MERET)]

for sor in terkep:
    for elem in sor:
        print(elem, end=' ')
    print()


def szigetek_szama(terkep):
    sziget_szam = 0
    for sor in range(len(terkep)):
        for oszlop in range(len(terkep[0])):
            if terkep[sor][oszlop] == 'x':
                sziget_szam += 1
                sziget_nullazo(terkep, sor, oszlop, sziget_szam)

    for sor in terkep:
        for elem in sor:
            print(elem, end=' ')
        print()
    return sziget_szam


def sziget_nullazo(terkep, sor, oszlop, sziget_szam):
    if sor >= 0 and sor < len(terkep) and \
            oszlop >= 0 and (oszlop < len(terkep[0]) and terkep[sor][oszlop] == 'x'):
        terkep[sor][oszlop] = sziget_szam
        sziget_nullazo(terkep, sor - 1, oszlop, sziget_szam)
        sziget_nullazo(terkep, sor + 1, oszlop, sziget_szam)
        sziget_nullazo(terkep, sor, oszlop - 1, sziget_szam)
        sziget_nullazo(terkep, sor, oszlop + 1, sziget_szam)

    print("Szigetek száma:", szigetek_szama(copy.deepcopy(terkep)))


"""  - https://www.youtube.com/watch?v=Low2PtXsb4g - """
