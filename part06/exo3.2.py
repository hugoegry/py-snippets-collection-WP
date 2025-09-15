def funA(s: str, n: int):
    if len(str(s)) >=  n:
        return True
    return False


def funB(s: str, n: int):
    resultat = ""
    for c in s: # .isalnum()
        if c.isalnum():
            resultat += c
    if funA(resultat, n):
        return True
    return False

def funC(s: str, n: int):
    resultat = ""
    for c in s:
        if c.isdigit():
            resultat += c
    if funA(resultat, n):
        return True
    return False


def passcheck(function, min_length: int, password: str):
    try:
        return function(password, min_length)
    except TypeError as e:
        print(f"Erreur de type dans la fonction : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def verif_password(password):
    return (
        passcheck(funC, 1, password)
        and passcheck(funB, 3, password)
        and passcheck(funA, 16, password)
    )

print(verif_password(input()))
