# fájlok olvasása és írása

valamilyen_tobbsoros_szoveg = '''\ 
Imagination is more important
than knowledge. Konwledge is limited.
Imagination encircles the world.
[Einstein]
'''

file = open("adatok.txt", "w")
file.write(valamilyen_tobbsoros_szoveg)
file.close()

file = open("adatok.txt", "r")
while True:
    egy_sor = file.readline()
    if len(egy_sor) ==0:
        break
    print(egy_sor)


# bármilyen ojjektum tárolása

import pickle

ez_egy_lista = ["gázlómadár", 999, False]
file1 = open("tároló.dat", "wb")   # eddig ugyanaz
pickle.dump(ez_egy_lista, file1)   # elrakta

del  ez_egy_lista                  # itt törölte
file1 = open("tároló.dat", "rb")
ez_egy_masik_lista = pickle.load(file1)
file1.close()

print(ez_egy_masik_lista)