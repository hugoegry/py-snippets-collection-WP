def bread():
    print("<////////// >")


def lettuce():
    print(" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")


def tomato():
    print(" O O O O O O ")


def ham():
    print("============")


def craftSandwiche(nb: int = 1):
    if type(nb) is int:
        if nb > 0:
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()
            craftSandwiche(nb - 1)
    else:
        print("Je ne peux pas faire ça !,")

craftSandwiche(2)
