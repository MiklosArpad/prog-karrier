
"""" függvények """

def koszones():
    print("Hello")

koszones()
koszones()
koszones()

def melyik_nagyobb_szam(a, b):   # ezek a formális paraméterek
    if a > b:
        print(a, "nagyobb")
    elif b > a:
        print(b, "nagyobb")
    else:
        print(a, "és", b, "egyenlő")

melyik_nagyobb_szam(12, 24)  # változók - aktuális paraméterek
print()
print("****************************************************************")
print()



""" Lokális és globális érték különbsége , a globális változó használata kerölendő"""


def nullazo_fuggveny(x):
    print("Ez jön kivülről:", x)
    x = 0
    print("Erre változi:", x)

x = 12
nullazo_fuggveny(x)
print("Globális változó:", x)

def globalis_nullazo_fuggveny():
    global x
    x = 0

globalis_nullazo_fuggveny()
print("Globális változó:, x")



# visszarérési értékkel rendelkező függvény - return kulcsszó

def add_vissza_a_nagyobb_szamot(a, b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "A két szám egyenlő nagyságú"
print(add_vissza_a_nagyobb_szamot(442, 155))

def ures_fuggveny_egyenlore():
    """ Itt lehet dokumentálni a függvényt (DocsStrings)"""
    pass
print(ures_fuggveny_egyenlore.__doc__)  # ezekkel lehet később infót kérni róla
help(ures_fuggveny_egyenlore())


"""  https://www.youtube.com/watch?v=7TsPxWcyVnQ  """