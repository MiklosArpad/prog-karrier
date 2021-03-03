
"""  Vezérlési szerkezetek
 szekció - elágazások - if
 """

szam1 = 236
tipp1 = int(input("Milyen számra tippelsz? "))

if tipp1 == szam1:
    print("Grat, elataláltad!")
elif tipp1 < szam1:
    print("A szám nagyobb, mint amire gondoltál")
else:
    print("A szám kisebb")



""" **************************************************************************"""

"""
szam2 = 236
futas2 = True

while futas2 == True:
    if tipp1 == szam2:
        print("Grat, elataláltad!")
        futas2 = False
    elif tipp1 < szam2:
        print("A szám nagyobb, mint amire gondoltál")
    else:
        print("A szám kisebb")
else:
    print("Vége a ciklusnak")


if True:
    print("Vége a proginak")

"""

for i in range(1, 5):
    print(i)
else:
    print("Vége aciklusnak")

# kilépés a cikluisból - break

while True:
    parancs = input("Írj be valamit")
    if parancs == "exit":
        break
    if len(parancs) < 2:
        print("A parancs túl rövid")
        continue
    print("Beírt parancs:", parancs)


"""   https://www.youtube.com/watch?v=tWPM4a58Ykc  """