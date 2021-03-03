
"""   Literálok    """
print('a')
print(13)
print(True, False)
print(24.2)
print('szöveg', "szöveg")

"""  Helyórzók """

print("Név: {0}, Kor: {1}".format("Béla", 24 ))

nev = "Géza"
kor = 28
print(f"Név: {nev}, Kor: {kor}")
print("Név: " + nev + ", Kor: " + str(kor))   # + típus konvertálás stringre

""" Kulcsszavas paraméterek """

print(1, 2, 3, sep="/", end="---")

"""  Sortörés vagy tabulátor """
print()
print("Hossz\tabb \n szö\\veg...")
print(r"Hossz\tabb \n szö\\veg...")  # ha r betű van előttük, akkor nem értékeli ki

