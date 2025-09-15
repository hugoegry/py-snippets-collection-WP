def funA(s: str, n: int):
    if len(str(s)) >=  n:
        return True
    return False


def funB(s: str, n: int):
    resultat = ""
    for c in s:
        if not (("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9")):
            resultat += c
    if funA(resultat, n):
        return True
    return False

def funC(s: str, n: int):
    resultat = ""
    for c in s:
        if ("0" <= c <= "9"):
            resultat += c
    if funA(resultat, n):
        return True
    return False


print(funC("azerr123", 4))