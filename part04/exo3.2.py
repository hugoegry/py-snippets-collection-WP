"""ctrl + /"""
alphabet: list[str] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]  # chiffrement de César
def chiffrementCesar(clee: int, text: str) -> str:
    textChiffre: str = ''
    for l in text.lower():
        if l in alphabet:
            position = alphabet.index(l)
            new_position = (position + clee) % len(alphabet) # modulo
            textChiffre += alphabet[new_position]
        else:
            textChiffre += l
    return textChiffre


def dechiffrementCesar(clee: int, textChiffre: str) -> str:
    textC: str = ""
    for l in textChiffre.lower():
        if l in alphabet:
            position = alphabet.index(l)
            new_position = (position - clee) % len(alphabet)  # modulo
            textC += alphabet[new_position]
        else:
            textC += l
    return textC


def casserCesar(texte: str):
    print(f"Texte chiffré : {texte}\n")
    for k in range(1, len(alphabet)+1):
        print(f"Cleé {k} > {dechiffrementCesar(k, texte)}")


clee: int = int(input("Entrez une clef : "))
textChiffre = chiffrementCesar(clee, input("Entrez une chaîne a chiffré : "))
print(textChiffre)
print(dechiffrementCesar(clee, textChiffre))
casserCesar(textChiffre)
