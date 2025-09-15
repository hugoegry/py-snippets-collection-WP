def summ(n: int):
    returnNb: int = 0
    for i in range(1, n+1):
        returnNb += i
    print(returnNb)

# summ(int(input()))


def somme_recursive(n: int) -> int:
    if n <= 0:
        return 0
    return n + somme_recursive(n - 1)

print(somme_recursive(int(input())))
