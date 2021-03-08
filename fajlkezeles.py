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