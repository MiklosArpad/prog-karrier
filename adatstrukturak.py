# adatstrukturák - listák

bevasarlolista = ["Liszt", "tej", "csoki"]
print("Ez itt a bevásárlólista", bevasarlolista)

bevasarlolista.append("Kakaó")
bevasarlolista.sort()

for listaelem in bevasarlolista:
    print(listaelem)

print("Az első listelem:", bevasarlolista[0])
del bevasarlolista[0]
print("Az első listelem:", bevasarlolista[0])

# tuple (olyan mint a lista, csak az elemei nem módosíthaóak)

allatok = ("zebra", "viziló", "oroszlán")
print(type(bevasarlolista))
print(type(allatok), len(allatok))
uj_allatok = allatok, "antilop", "cápa"
print(allatok)
print(uj_allatok, len(uj_allatok))
print(uj_allatok[0][1])

# szótárak - dictionary

adatbazis = {
    "Béla": "nela@gmail.com",
    "Károly": "karcsiVgmail.com",
    "Eszter": "eszti@gmail.com"
}
print(adatbazis["Béla"])
del adatbazis["Károly"]
print(len(adatbazis), adatbazis)
adatbazis["Eszter"] = "eszti&gmail.com"

for nev, email in adatbazis.items():
    print(nev, email)

if "Béla" in adatbazis:
    print("jelen")

# halmazok - set

orszagok = ["USA", "UK", "RU", "BG", "DK", "DK", "DK", "HUN", "SK"]
orszagok_halmaza = set(orszagok)
print("Lista:", orszagok)
print("Halamz:", orszagok_halmaza)
print("NL" in orszagok_halmaza)

tobb_orszag_halmaz = orszagok_halmaza.copy()
tobb_orszag_halmaz.add("CH")

print(tobb_orszag_halmaz.issuperset(orszagok_halmaza))         # részhalmaz-e ???
orszagok_halmaza.remove("UK")
print(orszagok_halmaza & tobb_orszag_halmaz)                   # halamzok metszete
print(orszagok_halmaza.intersection(tobb_orszag_halmaz))

"""  https://www.youtube.com/watch?v=oXsVjzs5psg   """