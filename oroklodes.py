# öröklés

class Egyetemi_hallgato:

    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor
        print(self.nev, "létrehozva.")

    def adatok_kiirasa(self):
        print(f"Név: {self.nev}, kor: {self.kor}")


# több hallgató létrehozása

class Bolcsesz(Egyetemi_hallgato):
    def __init__(self, nev, kor, kedvenc_iro):
        Egyetemi_hallgato.__init__(self, nev, kor)  # eddig ugyanaz
        self.kedvenc_iro = kedvenc_iro  # ez már nem öröklódés, ez új információ

    def adatok_kiirasa(self):
        Egyetemi_hallgato.adatok_kiirasa(self)  # eddig ugyanaz
        print("Kedvenc írója", self.kedvenc_iro, end="\n\n")  # ez már nem öröklódés, ez új információ


# egy újabb hallgató típus

class Mernok(Egyetemi_hallgato):
    def __init__(self, nev, kor, kedvenc_tudos):
        Egyetemi_hallgato.__init__(self, nev, kor)  # eddig ugyanaz
        self.kedvenc_tudos = kedvenc_tudos  # ez már nem öröklódés, ez új információ

    def adatok_kiirasa(self):
        Egyetemi_hallgato.adatok_kiirasa(self)  # eddig ugyanaz
        print("Kedvenc tudósa:", self.kedvenc_tudos, end="\n\n")  # ez már nem öröklódés, ez új információ


# most létrehozunk egy - egy hallgatót a két típusból

hallgato1 = Bolcsesz("Ildiko", 44, "Agatha Christie")
hallgato2 = Mernok("Árpád", 48, "Neumann János")

print()

hallgatok = [hallgato1, hallgato2]
for hallgato in hallgatok:
    hallgato.adatok_kiirasa()

""" https://www.youtube.com/watch?v=vZhfkCLJ42k   """