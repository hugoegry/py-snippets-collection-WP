voyelles: list[str] = ['a', 'e', 'i', 'o', 'u', 'y']
saisie: str = input("Entrez un entier et une chaîne séparés par un espace : ")
p = saisie.split(maxsplit=1)
entier: int = int(p[0])
hasAnyVowel: bool = False
if entier != 0:
    for l in p[1]:
        if voyelles.__contains__(l.lower()):
            print(entier)
            hasAnyVowel = True
            break
    if entier >= 42 and not hasAnyVowel:
        print(entier)
    elif not hasAnyVowel:
        print(p[1])