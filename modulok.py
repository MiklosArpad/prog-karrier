
# modulok

import sys
import os
import math

print("A parncssoros indítással átadott paraméterek listája:")
for i in sys.argv:
    print(i)

print(os.getcwd())

print("Négyzetgyök:", math.sqrt(16))

if __name__ == "__main__":
    print("Főprogramként indulok")
else:
    print("Valahonann inportáltak, mint külső modul")

def sajat_modul_fuggvenye():
    print("Importálható modul")
    