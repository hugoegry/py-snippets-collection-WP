def funA(s: str, n: int) -> bool:
    if len(str(s)) >=  n:
        return True
    return False


def funB(s: str, n: int) -> bool:
    resultat = ""
    for c in s:
        if c.isalnum():
            resultat += c
    if funA(resultat, n):
        return True
    return False


def funC(s: str, n: int) -> bool:
    resultat = ""
    for c in s:
        if c.isdigit():
            resultat += c
    if funA(resultat, n):
        return True
    return False


def passcheck(function, min_length: int, password: str) -> bool:
    return function(password, min_length)


def verif_password(password) -> bool:
    return (
        passcheck(funC, 1, password)
        and passcheck(funB, 3, password)
        and passcheck(funA, 16, password)
    )


print(verif_password(input()))
