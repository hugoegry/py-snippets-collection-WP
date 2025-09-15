# ça merge les deux liste en metant les element a la fin
uneListe: list[int] = [1,2,3,4,5]
resultat: int = 0
for chiffre in uneListe:
    if resultat != 0:
        resultat *= chiffre
    else:
        resultat += chiffre
print(resultat)
