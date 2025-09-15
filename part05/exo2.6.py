a = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
print(a)

# pour chaque x dans la liste on test si il est divisible par 2 si c est le cas on remplace ça valeur par la valeur de ça division par 2
# sinon sinon on remplace ça valeur par ça valeur * 2