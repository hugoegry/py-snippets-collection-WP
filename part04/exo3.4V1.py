# enumerate()asocie les element a leur index
alphabet: list[str] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]  # chiffrement de César
def chiffrementVigenere(clee: str, text: str) -> str:
    if(len(clee) != len(text)):
        return 'la clee doit avoir la meme longueur que le text'
    textChiffre: str = ''
    for i, l in enumerate(text.lower()):
        position = alphabet.index(l)
        cleePosition = alphabet.index(clee[i])
        new_position = (position + cleePosition) % len(alphabet)  # modulo
        textChiffre = textChiffre + alphabet[new_position]
    return textChiffre


def dechiffrementVigenere(clee: str, textChiffre: str) -> str:
    textC: str = ""
    for i, l in enumerate(textChiffre.lower()):
        position = alphabet.index(l)
        cleePosition = alphabet.index(clee[i])
        new_position = (position - cleePosition) % len(alphabet)  # modulo
        textC = textC + alphabet[new_position]
    return textC


def geneCombinaison(longueur: int) -> list[str]:
    combinaisons: list[str] = [""]
    for i in range(longueur):
        newL: list[str] = []
        for prefix in combinaisons:
            for l in alphabet:
                newL.append(prefix + l)
        combinaisons = newL
    return combinaisons


def casserVigenere(texte: str):
    i: int = 1
    print(f"Texte chiffré : {texte}\n")
    lenClee = len(texte)
    allPosibility = geneCombinaison(lenClee)
    for k in allPosibility:
        print(f"Cleé N{i} ({k}) > {dechiffrementVigenere(k, texte)}")
        i += 1


clee: str = input("Entrez une clef : ")
textChiffre = chiffrementVigenere(clee, input("Entrez une chaîne a chiffré : "))
print(textChiffre)
print(dechiffrementVigenere(clee, textChiffre))
casserVigenere(textChiffre)