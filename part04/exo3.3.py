# enumerate()asocie les element a leur index
alphabet: list[str] = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]  # chiffrement de César
def chiffrementVigenere(clee: str, text: str) -> str:
    if(len(clee) != len(text)):
        return 'la clee doit avoir la meme longueur que le text'
    textChiffre: str = ''
    for i, l in enumerate(text.lower()):
        if l in alphabet:
            position = alphabet.index(l)
            cleePosition = alphabet.index(clee[i])
            new_position = (position + cleePosition) % len(alphabet)  # modulo
            textChiffre += alphabet[new_position]
        else:
            textChiffre += l
    return textChiffre


def dechiffrementVigenere(clee: str, textChiffre: str) -> str:
    textC: str = ""
    for i, l in enumerate(textChiffre.lower()):
        if l in alphabet:
            position = alphabet.index(l)
            cleePosition = alphabet.index(clee[i])
            new_position = (position - cleePosition) % len(alphabet)  # modulo
            textC += alphabet[new_position]
        else:
            textC += l
    return textC

clee: str = input("Entrez une clef : ")
textChiffre = chiffrementVigenere(clee, input("Entrez une chaîne a chiffré : "))
print(textChiffre)
print(dechiffrementVigenere(clee, textChiffre))
