def bread () :
    print( "<////////// >" )
def lettuce():
    print( " ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ " )
def tomato() :
    print( " O O O O O O " )
def ham ():
    print("============")

def vegetable():
    print("%%%%%%%%%%")

def craftSandwiche(nb: int = 1, isVegi: bool = False):
    if type(nb) is int:
        if nb > 0:
            bread()
            lettuce()
            tomato()
            if not isVegi:
                ham()
                ham()
            else:
                vegetable()
                vegetable()
            bread()
            craftSandwiche(nb-1, isVegi)
    else:
        print("Je ne peux pas faire ça !,")

craftSandwiche(2)
