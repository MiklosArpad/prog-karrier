
# alapértelemezett paraméter
# kulcsazavas paraméter

def uzenet_sokszorozo(uzenet, szorzo = 3):
    print(uzenet * szorzo)

uzenet_sokszorozo("Lila Liba ")
uzenet_sokszorozo("Lila Liba ", 4)

def f(a, b=2, c=3):
    print(f"A={a}, B={b}, C={c}")

f(11, 12, 13)
f(c=1, b=2, a=3)

# változó számú paraméter átadása a függvényeknek

#   * nélül: kötelező paraméter
#   1 *: opcionális paraméter
#   2 *: opcionális - kulcsszavas paraméter

def fuggveny(a=111, *szamok, **mellekek):
    print("A=", a)

    for szam in szamok:
        print(szam)

    for kulcsszo, ertek, in mellekek.items():
        print(kulcsszo, ertek)

fuggveny(222, 1, 2, 3,4, 5, Bela=1234, Geza=5678, Janka=1357)


""" https://www.youtube.com/watch?v=zP6Cko_fm8E """

