import re
import unicodedata


def nettoyer_chaine(texte: str) -> str:
    # 1. Supprimer accents
    texte = unicodedata.normalize(
        "NFD", texte
    )  # décompose les lettres accentuées en lettre + accent séparé.
    texte = "".join(
        c for c in texte if unicodedata.category(c) != "Mn"
    )  # enlève tous les accents, ne gardant que la lettre de base.

    texte = re.sub(r"[^a-zA-Z0-9]", "", texte)  # Supprimer tout sauf lettres/chiffres
    return texte.lower()


def est_palindrome_recursive(texte: str) -> bool:
    if len(texte) <= 1:
        return True
    if texte[0] != texte[-1]:
        return False
    return est_palindrome_recursive(texte[1:-1])


def main():
    if est_palindrome_recursive(nettoyer_chaine(input("Entrez une chaîne : "))):
        print("C est un palindrome")
    else:
        print("Ce n est pas un palindrome")


main()

# exemple never odd or even // A Santa Lived As a Devil at NASA
