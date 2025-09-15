entier: int = int(input('saisir un entier : '))
if entier == 42  :
    print('a')
elif entier <= 21:
    print('b')
elif (entier % 2) == 0:
    print('c')
elif (entier / 2) < 21:
    print('d')
elif (entier % 2) != 0 and entier <= 45:
    print('e')
else:
    print('f')
