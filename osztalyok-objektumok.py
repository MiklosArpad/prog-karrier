

# osztályok és objektumok

class Ember:
    def __init__(self, ember_nev):
         self.nev = ember_nev

    def koszones(self):
        print(f"Hellő én {self.nev} vagyok!")

egy_ember = Ember("Árpád")
egy_ember.koszones()





class Munkatárs:

    """ Munkatársak regisztrálása """

    ennyi_munkatars_lett_letrehozva = 0        # osztályváltozó, ebből csak egy van

    def __init__(self, munkatars_nev):
        self.nev = munkatars_nev
        Munkatárs.ennyi_munkatars_lett_letrehozva += 1   # ha létrehozunk egyet

    def koszones(self):
        print(f"Hellő én {self.nev} vagyok!")

    def vege_a_muszaknak(self):
        Munkatárs.ennyi_munkatars_lett_letrehozva -= 1

    @classmethod
    def hányan_dolgoznak_még(cls):
        print(cls.ennyi_munkatars_lett_letrehozva, "ember dolgozik még.")

egy_munkatars = Munkatárs("Árpád")
egy_munkatars.koszones()
masik_munkatars = Munkatárs("Ildikó")
masik_munkatars.koszones()

Munkatárs.hányan_dolgoznak_még()
egy_munkatars.vege_a_muszaknak()
Munkatárs.hányan_dolgoznak_még()
masik_munkatars.vege_a_muszaknak()
Munkatárs.hányan_dolgoznak_még