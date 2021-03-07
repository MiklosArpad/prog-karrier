

# szekvenciák megcímzése

lista =["Árpád", "Benő", "Jenő", "Áron", "Bence", "Balázs"]
csak_egy_szoveg = "Csak egy szöveg, és kész!"

lista_masolat = lista[:]

print(lista.index)
print(lista_masolat.index)

del lista[0]
print(lista)
print(lista_masolat)

print(lista[0])
print(lista[2])
print(lista[1])
print(lista[-1])
print(lista[-2])
print(csak_egy_szoveg[0])
print(csak_egy_szoveg[1])
print(csak_egy_szoveg[2])
print(csak_egy_szoveg[3])
print(csak_egy_szoveg[-1])
print()
print(lista[1:3])
print(lista[2:])
print(lista[1:-1])
print(lista[:])  # ez is a teljes lista
print()
print(csak_egy_szoveg[2:12])  # ez a 3. kararktetől a 12. karakterig ír ki
print(csak_egy_szoveg[::-1])   # visszafelé
print(csak_egy_szoveg[::2])    # kettesével irat ki
print()

print(csak_egy_szoveg.startswith("Cs"))
print("egy" in csak_egy_szoveg)
print(csak_egy_szoveg.find("egy"))
elvalaszto_karakter = " /// "
print(elvalaszto_karakter.join(lista))